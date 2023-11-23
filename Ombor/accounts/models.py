from django.db import models
from django.contrib.auth.models import AbstractUser

class Ombor(AbstractUser):
    ism = models.CharField(max_length=30, blank=True)
    nom = models.CharField(max_length=20, blank=True)
    manzil = models.CharField(max_length=30, blank=True)
    soha = models.CharField(max_length=30, blank=True)
    tel = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.username}"

