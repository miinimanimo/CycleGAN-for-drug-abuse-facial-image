# views.py
import os
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image
import tensorflow as tf
import numpy as np
import io
from django.conf import settings
import base64
import tensorflow_addons as tfa
from tensorflow_examples.models.pix2pix import pix2pix
import glob
from rembg import remove

# Django 설정 모듈의 Python import path를 설정합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cycle1.settings')

# Django 설정을 로드합니다.
application = get_wsgi_application()

# 체크포인트 경로
checkpoint_dir = os.path.join(settings.BASE_DIR, 'cycle1', 'models', 'train_90_600')

# 모델 초기화
OUTPUT_CHANNELS = 3

generator_g = pix2pix.unet_generator(OUTPUT_CHANNELS, norm_type='instancenorm')

# 체크포인트에서 가장 최근의 체크포인트를 로드
checkpoint = tf.train.Checkpoint(generator_g=generator_g)
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))

def preprocess_image(image):
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, [256, 256])
    image = (image / 127.5) - 1
    image = tf.expand_dims(image, 0)
    return image

@csrf_exempt
def generate(request):
    if request.method == 'POST':
        image = request.FILES['image'].read()

        # Remove the background of the image
        image_without_bg = remove(image)

        # Convert to PIL Image object
        image = Image.open(io.BytesIO(image_without_bg)).convert("RGB")
        image = img_to_array(image)
        image = preprocess_image(image)
        generated_image = generator_g(image, training=False)

        # Convert the generated image to PIL image
        generated_image = tf.squeeze(generated_image, [0])  # Remove the batch dimension
        generated_image = tf.cast((generated_image + 1) * 127.5, tf.uint8)  # Normalize the tensor values to [0, 255] and convert it to uint8
        generated_image = Image.fromarray(generated_image.numpy())  # Convert the tensor to a PIL image

        # Convert the PIL image to image file
        buffer = io.BytesIO()
        generated_image.save(buffer, format='JPEG')
        img_str = base64.b64encode(buffer.getvalue()).decode()

        return JsonResponse({'image': img_str})
