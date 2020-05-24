from tkinter import Image

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='/static/img/avatar.png')
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='', null=True)
    email = models.EmailField(default='none@email.com')
    bio = models.TextField(default='')
    is_contributor = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    country = models.CharField(max_length=255, default='')
    field = models.CharField(max_length=255, default='')


    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
