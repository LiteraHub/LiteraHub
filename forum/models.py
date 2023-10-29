from django.db import models
from django.contrib.auth.models import User
from buku.models import Buku
    
thread_choices = (
    ('thread','Thread Baru'),
    ('recommend', 'Thread Rekomendasi Buku'),
    ('penulis', 'Thread Penulis'),
)
class Thread(models.Model): #Threads in recommendation
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    forum = models.CharField(max_length=9, choices=thread_choices, default='thread', null=True)
    date = models.DateTimeField(auto_now_add=True)
    buku = models.ForeignKey(Buku, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def post_amount(self):
            return Post.objects.filter(threads=self).count()
    
    @property
    def last_post(self):
        return Post.objects.filter(threads=self).latest("date")
    
    @property
    def book_title(self):
        return self.buku.title if self.buku else None

    @property
    def book_cover(self):
        if self.buku and self.buku.img:
            return self.buku.img
        else:
            return '/static/forum/default_cover.jpg'
    
class Post(models.Model): #posts
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)