from django.db import models
from django.contrib.auth.models import AbstractUser

from core.managers import UserManager


class MyUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()