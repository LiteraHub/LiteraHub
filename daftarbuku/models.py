from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from buku.models import Buku

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    review = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True)
