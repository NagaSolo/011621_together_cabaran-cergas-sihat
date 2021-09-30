from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='images/profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'