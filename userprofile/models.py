from django.db import models
from django.contrib.auth.models import AbstractUser
from organisation.models import Service


class UserProfile(AbstractUser):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

