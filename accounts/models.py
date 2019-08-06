from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    bio = models.TextField(blank=True)
    website_url = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)


post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)