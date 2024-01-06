from django.db import models
from ast import Pass
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
import uuid
from embed_video.fields import EmbedVideoField


# Create your models here.

# Create your models here.
class Profile(models.Model):
      user = models.OneToOneField(User,on_delete=models.CASCADE)
      forget_password_token = models.CharField(max_length=100)
      is_verified = models.BooleanField(default=False)
      create_at=models.DateTimeField(auto_now_add=True)
  


def __str__(self):
        return self.user.username    



class Category(models.Model):
    name = models.CharField(max_length=100)

    
class Phone(models.Model):
    phone = PhoneField(blank=False)



    

class listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length =10, blank =True)
    website = models.URLField(max_length=200)
    specification = models.CharField(max_length=250)
    heading = models.TextField()
    about = models.TextField()
    youtub =  EmbedVideoField()
    specification1 = models.TextField()
    specification2 = models.TextField()
    specification3 = models.TextField()
    specification4 = models.TextField()
    specification5 = models.TextField()
    address = models.CharField(max_length=250)
    open_timing  = models.CharField(max_length=250)
    background_image = models.ImageField()
    address_image = models.ImageField()
    gallery_img1 = models.ImageField(upload_to='listing')
    gallery_img2 = models.ImageField(upload_to='listing')
    gallery_img3 = models.ImageField(upload_to='listing')
    gallery_img4 = models.ImageField(upload_to='listing')
    gallery_img5 = models.ImageField(upload_to='listing')
    keywords = models.TextField()

    def __str__(self):
        return str(self.name) 
class Enquire(models.Model):
     first_name = models.CharField(max_length=250)
     last_name = models.CharField(max_length=250)
     Business_name = models.CharField(max_length=250)
     Business_categrey = models.CharField(max_length=250)
     email = models.EmailField(unique=True)
     phone = PhoneField(blank=True)
     address = models.CharField(max_length=250) 

     def __str__(self):
        return str(self.id) 


class Review(models.Model):
    listings = models.ForeignKey( listing, on_delete=models.CASCADE)
    name =  models.CharField(max_length=250)
    user =  models.ForeignKey(User,models.CASCADE)
    email  = models.EmailField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) 

