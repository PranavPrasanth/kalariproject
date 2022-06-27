from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_type = models.CharField(max_length=15,default='admin')
    def __str__(self):
        return self.username


class mykalari(models.Model):

    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True, default='profile_pics/default.jpg')


def __str__(self):
    return self.name


class users(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True, default='profile_pics/default.jpg')


def __str__(self):
    return self.name

# Create your models here.
