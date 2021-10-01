from django.conf import settings
from django.db import models

from django.contrib.auth.models import User

# signals
from django.dispatch import receiver  # add this
from django.db.models.signals import post_save  # add this

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='images/profile_pics')

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
	    if created:
	    	Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
    	instance.profile.save()

    def __str__(self) -> str:
        return f'{self.user.username} Profile'