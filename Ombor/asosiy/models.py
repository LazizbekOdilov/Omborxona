from django.db import models

from accounts.models import Omborxona


class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    olchov = models.CharField(max_length=50)
    narx = models.PositiveIntegerField()
    miqdor = models.PositiveSmallIntegerField()
    kelgan_sana = models.DateField(null=True, blank=True)
    ombor = models.ForeignKey(Omborxona, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}, {self.brend}"


class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    ombor = models.ForeignKey(Omborxona, on_delete=models.CASCADE)
    qarz = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.ism}, {self.nom}"