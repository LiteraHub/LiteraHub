from django.urls import path
from forum.views import show_forum, add_post

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('add_post', add_post, name='add_post'),
]