from django.urls import path
from main import views

urlpatterns = [
    path('generate/', views.generate),
]

