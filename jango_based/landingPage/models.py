from django.db import models

from django.contrib.auth.models import User

# # Create your models here.
# class Profile(models.Model):
#     mobile_no = models.CharField(max_length=20)
#     pro_pic = models.ImageField(upload_to='users/pro_pics', blank=True, null=True)

#     user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

#     status = models.CharField(max_length=10, blank=True, null=True, default='False')

#     def __str__(self):
#         return self.user.username