from django.db import models
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# # Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_image = models.FileField(default="user-profile-default.jpg", upload_to='profileImage/', null=True, blank=True)

    def __str__(self):
        return self.user.username








# def create_profile(self, **kwargs):
#     Profile.objects.create(
#         user=self,
#         **kwargs
#     )
#
#
# auth.models.User.add_to_class('create_profile', create_profile)

# class UserProfile(models.Model):
#     # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_image = models.FileField(upload_to='profileImage/', blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#
# post_save.connect(create_profile, sender=User)


# student_id = models.CharField(max_length=20)
# photo = models.ImageField(upload_to='profileImage/', blank=True)

# def __str__(self):
#     return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = Profile.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)
