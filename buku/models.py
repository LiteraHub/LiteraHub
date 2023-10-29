from django.db import models

class Buku(models.Model):
    isbn = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    img = models.TextField(null=True, blank=True)
    is_ready = models.BooleanField(default=True)
