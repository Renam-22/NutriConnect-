from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    bmi    = models.FloatField(null=True)
    date_of_birth = models.DateField(null=True)
    goal = models.CharField(max_length=200,null=True)
    phone_no = models.CharField(max_length=15,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',default='def_profile.jpg')
