from django.db import models
from django.contrib.auth.models import User
from buku.models import Buku

class Thread(models.Model): #Threads in recommendation
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    buku = models.ForeignKey(Buku, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def post_amount(self):
            return Post.objects.filter(threads=self).count()
    
    @property
    def last_post(self):
        return Post.objects.filter(threads=self).latest("date")
    
class Post(models.Model): #posts
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)