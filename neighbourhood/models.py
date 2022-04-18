import imp
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from phone_field import PhoneField
from cloudinary.models import CloudinaryField


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hood",null=True)
    hood_logo =CloudinaryField('hood_logo')
    description = models.TextField()
    health_tell = PhoneField(null=True, blank=True)
    police_number = PhoneField(null=True, blank=True)
    area_administrator = models.CharField(max_length=100,null=True)