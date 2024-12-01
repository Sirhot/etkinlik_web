from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    location = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = [
        ("E", "Erkek"),
        ("K", "Kadın")
    ]
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True, 
        null=True
    )
    phone_number = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to="images",default="images/user.jpg")#make migration

    def __str__(self):
        return self.username

class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")