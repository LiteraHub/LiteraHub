from django.contrib.auth.models import User
from buku.models import Buku
from django.db import models

# Create your models here.
class PeminjamanBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    tanggal_peminjaman = models.DateField(auto_now_add=True)
    tanggal_pengembalian = models.DateField()
    is_dikembalikan = models.BooleanField()
    gambarBuku = models.TextField()
        