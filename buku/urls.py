from django.urls import path
from buku.views import get_books

app_name = 'buku'

urlpatterns = [
    path('', get_books, name = 'get_books'),
]
