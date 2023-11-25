from django.db import models
from accounts.models import Omborxona
from asosiy.models import Mahsulot, Mijoz

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    miqdor = models.PositiveSmallIntegerField()
    sana = models.DateTimeField()
    summa = models.PositiveIntegerField()
    tolangam_summa = models.PositiveIntegerField()
    nasiya = models.PositiveIntegerField()
    ombor = models.ForeignKey(Omborxona, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.summa}"
