from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
                         
class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=CASCADE)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)
    
    def __str__(self):
        return self.mobile


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    username=models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return self.username
