from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager


# Create your models here.
class CustomUserModel(AbstractUser):
    email= models.EmailField(unique=True)


    USERNAME_FIELD ="email"
    REQUIRED_FIELDS =[]


    object = CustomUserManager()