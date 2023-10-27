from django.urls import path
from peminjamanbuku.views import *

app_name = 'peminjamanbuku'

urlpatterns = [
        path('show-peminjaman/', show_peminjaman, name='show_peminjaman'),
        path('get-pinjem/', get_pinjam_json, name='get_pinjam_json'),
        path('get-buku-item/', get_buku_json, name='get_buku_json'),
        path('pinjam_buku/', pinjam_buku, name='pinjam_buku'),
        path('get-buku-by-id/<int:id>/', get_buku_by_id, name='get_buku_by_id'),
]