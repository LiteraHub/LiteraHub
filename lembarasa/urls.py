from django.urls import path
from lembarasa.views import show_lembarasa
from lembarasa.views import show_json_buku, show_json_mybuku
from lembarasa.views import create_ajax, get_buku_json, delete_ajax, get_mybuku_json_id
from lembarasa.views import create_buku_flutter, show_json_mybuku_user, get_semua_buku_json, delete_buku_flutter

app_name = 'lembarasa'

urlpatterns = [
    path('', show_lembarasa, name='show_lembarasa'),
    path('json-buku/', show_json_buku, name='show_json_buku'),
    path('json-mybuku/', show_json_mybuku, name='show_json_mybuku'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('get-buku/', get_buku_json, name='get_buku_json'),
    path('delete-ajax/<int:id>/', delete_ajax, name='delete_ajax'),
    path('get-mybuku-id/<int:id>/', get_mybuku_json_id, name='get_mybuku_json_id'),
    path('create-flutter/', create_buku_flutter, name='create_buku_flutter'),
    path('json-mybuku-user/', show_json_mybuku_user, name='show_json_mybuku_user'),
    path('get-semua-buku/', get_semua_buku_json, name='get_semua_buku_json'),
    path('delete-flutter/', delete_buku_flutter, name='delete_buku_flutter'),
]
