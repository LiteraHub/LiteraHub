from django.urls import path
from . import views
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_thread/', views.add_thread, name='add_thread'),
    path('threads/', to_thread, name='threads'),
    path('get_threads/', views.get_threads, name='get_threads'),
    path('get_books_json/', get_books_json, name='get_books_json'),
    path('get_post/', views.get_post, name='get_post'),
    path('get_time/', get_time, name='get_time'),
    path('get_buku_title/', get_buku_title, name='get_buku_title'),
]