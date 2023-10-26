from django.urls import path
from lembarasa.views import show_lembarasa

app_name = 'lembarasa'

urlpatterns = [
    path('', show_lembarasa, name='show_lembarasa'),
]
