# DrugSafe - CycleGAN(for-drug-abuse-facial-image)
The model checkpoint files are too large, so I'm attaching them via Dropbox link. Download 90-600 and place it in the 'models' folder under 'cycle1'. If you want to use a different checkpoint, modification of the views.py code is necessary.


# AI

At DrugSafe, this serves to process the user's facial input, predict potential facial changes from drug use, and present these predictions to communicate risks.

# Technology
Code - Tensorflow </br>
Distribution - Django </br>


## What is DrugSafe?
<img width="317" alt="image" src="https://github.com/hyeok55/solution_challenge_2024/assets/67605795/481a7265-2721-4f0c-8cec-b8a4d4445c10">


The drug problem is serious worldwide. It is a project that helps to inform and prevent the seriousness and risk of drug addiction in order to solve these problems and create a healthier society. DrugSafe provides prediction of the risk of drug abuse and side effects of facial aging when drug abuse is performed, and lists drug mortality, interest, and drugs by type.


# Development process
## Building a CycleGAN model
"cycle_gan.ipynb", located in the same location as the Readme, is the code for model training.

Initially, the model was designed to predict facial changes based on the duration of drug use. We intended to allow users on the website to specify the type of drug and the duration of use. However, there were issues of privacy with facial photos, and it was not easy to find data. We contacted the relevant data center for a dataset of faces according to the duration of drug use, but we were not granted access. Therefore, we labeled the data by googling, but there wasn't much. We had to build a model with only 30 sets of before and after drug use photos.

I tried to build a model from scratch using PyTorch, which I am more familiar with. However, I failed to build the model because I could not properly understand the features. This is the first Style GAN model I built, and as you can see, it generated this as a human face.
--사진

I studied a bit more and built a model based on two new papers.

https://arxiv.org/pdf/2304.06106.pdf

https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/generative/cyclegan.ipynb

The first paper explained how we should design the model, and we referred to the tensorflow code in the second paper.

When looking at before and after pictures of people who use drugs, they usually develop freckles. I got an idea from this. The second paper is about a model that simply transforms horses into zebras. I thought that the generation of spots is similar to the development of freckles. Therefore, I began to construct a CycleGAN model based on the tensorflow code in the second paper.

When I first trained, the model kept turning off during training, so I proceeded with the training on a different computer. After training, the model performance was not good, so I thought that the background of the model picture affected the learning, so I added a code to erase the background and started learning again. Initially, we set 20 sets of before and after facial photos as the training set and 10 sets of before and after facial photos as the test set. However, it was decided that it would be better to increase the amount of training set because the data was limited to a very small amount. Therefore, we used 25 sets of before and after facial photos as the training set and 5 sets of before and after facial photos as the test set.

At first, the lambda value was set to 1, so we changed the epoch value and proceeded with the training. However, the pictures were broken, so we increased the lambda value and proceeded with the training. We kept changing the parameters to find a model with good performance.
lambda-epoch
1-300

120-1000

150-1000

25-300

85-300

90-600

After several attempts, I was able to construct a decent model.

Image sources
https://rehabs.com/explore/faces-of-addiction/

https://wjla.com/news/crime/gallery/photos-before-and-after-faces-of-addiction-pictures-show-impact-of-drugs-on-men-women?photo=5

## Distribution
After selecting the model, I deployed it using a Django server. Initially, I tried to deploy the model by saving it in .h5 format, but I encountered version compatibility issues, so the deployment did not go smoothly. As a result, I attempted to deploy the model using the saved checkpoints. I used a method of sending and receiving photos as strings using base64 encoding. I was successful in deploying using Google Compute Engine in the Google Cloud Console.


## API
### generate image API
main/generate/ 


