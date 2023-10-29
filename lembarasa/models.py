from django.db import models
from django.contrib.auth.models import User
from buku.models import Buku

# Create your models here.
class MyBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    isi = models.TextField()