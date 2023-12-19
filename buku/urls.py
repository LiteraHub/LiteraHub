from django.urls import path
from buku.views import get_books, replace_img

app_name = 'buku'

urlpatterns = [
    path('', get_books, name = 'get_books'),
    path('replace_img/', replace_img, name = 'replace_img'),
]
