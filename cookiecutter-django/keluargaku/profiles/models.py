from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from PIL import Image
from django.db.models.fields.related import OneToOneField

class ProfileImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='images/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'