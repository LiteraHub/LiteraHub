from django.urls import path
from reservasi.views import create_reservasi_flutter, get_reservasi_json_flutter, selesai_flutter, show_page_reservasi, buat_reservasi, get_buku_json, katalog, get_tempat_baca, get_reservasi_json, selesai

app_name = 'reservasi'

urlpatterns = [
     path('', show_page_reservasi, name='show_page_reservasi'),
     path('buat-reservasi', buat_reservasi, name='buat_reservasi'),
     path('get-buku-json', get_buku_json, name='get_buku_json'),
     path('katalog', katalog, name='katalog'),
     path('get-tempat-baca', get_tempat_baca, name='get_tempat_baca'),
     path('get-reservasi-json', get_reservasi_json, name='get_reservasi_json'),
     path('selesai/<int:reservasi_id>', selesai, name='selesai'),
     path('create-flutter/', create_reservasi_flutter, name='create_reservasi_flutter'),
     path('selesai-flutter/', selesai_flutter, name='selesai_flutter'),
     path('get-reservasi-flutter/', get_reservasi_json_flutter, name='get_reservasi_json_flutter'),
]