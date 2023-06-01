from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from rest_framework.authtoken.models import Token

# Creating tokens for each user
# https://www.django-rest-framework.org/api-guide/authentication/#generating-tokens
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

