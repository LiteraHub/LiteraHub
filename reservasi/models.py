from django.db import models
from django.contrib.auth.models import User
from buku.models import Buku

class TempatBaca(models.Model):
     id_tempat = models.IntegerField(unique=True)
     dipesan = models.BooleanField(default=False)
     
class Reservasi(models.Model):
     nama = models.CharField(max_length=50)
     no_hp = models.CharField(max_length=15)
     buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
     tempat_baca = models.ForeignKey(TempatBaca, on_delete=models.CASCADE)
     durasi_baca = models.DurationField()

# Create your models here.
