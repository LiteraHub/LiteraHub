from django.urls import path
from reservasi.views import show_page_reservasi, buat_reservasi, receipt, get_buku_json

app_name = 'reservasi'

urlpatterns = [
     path('', show_page_reservasi, name='show_page_reservasi'),
     path('buat-reservasi', buat_reservasi, name='buat_reservasi'),
     path('receipt/<int:reservasi_id>', receipt, name='receipt'),
     path('get-buku-json', get_buku_json, name='get_buku_json')
]