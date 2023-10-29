import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from buku.models import Buku

class TempatBaca(models.Model):
     id_tempat = models.IntegerField(unique=True)
     dipesan = models.BooleanField(default=False)
     
class Reservasi(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     nama = models.CharField(max_length=50)
     no_hp = models.CharField(max_length=14)
     buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
     tempat_baca = models.ForeignKey(TempatBaca, on_delete=models.CASCADE)
     tanggal = models.DateField(default=datetime.date.today)
     jam = models.TimeField(default=timezone.now)     
     durasi_baca = models.CharField(max_length=1)
     selesai = models.BooleanField(default=False)

# Create your models here.
