from django.urls import path
from . import views
from forum.views import *

app_name = 'forum'

urlpatterns = [
<<<<<<< HEAD
    path('', views.show_forum, name='show_forum'),
    path('posts/<int:id>', views.show_posts, name='show_posts'),
    path('add_thread/', views.add_thread, name='add_thread'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_thread_flutter/', views.add_thread_flutter, name='add_thread_flutter'),
    path('add_post_flutter/', views.add_post_flutter, name='add_post_flutter'),
    path('json_thread/', views.get_json_threads, name='get_json_threads'),
    path('json_posts/<int:id>/', views.get_json_posts, name='get_json_posts'),
    path('json_buku/', views.get_json_buku, name='get_json_buku'),
    path('buku_title/<str:title>/', views.get_buku_by_title, name='get_buku_by_title'),
    path('buku_id/<int:id>', views.get_buku_by_id, name='get_buku_by_id'),
=======
    path('', show_forum, name='show_forum'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_thread/', views.add_thread, name='add_thread'),
    path('threads/', to_thread, name='threads'),
    path('get_threads/', views.get_threads, name='get_threads'),
    path('get_books_json/', get_books_json, name='get_books_json'),
    path('get_post/', views.get_post, name='get_post'),
    path('get_time/', get_time, name='get_time'),
    path('get_buku_title/', get_buku_title, name='get_buku_title'),
>>>>>>> 46520bf9e69852afa2b7d4b50b417c5980cfedb2
]