from django.db import models
from django.contrib.auth.models import User
from buku.models import Buku

class Forum(models.Model): #recommendations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=255)
    date_updated = models.DateTimeField(auto_now_add=True)
    
class Thread(models.Model): #Threads in recommendation
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
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