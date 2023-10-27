from datetime import datetime
from django.shortcuts import render
from buku.models import Buku
from peminjamanbuku.models import PeminjamanBuku
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_peminjaman(request):
    dataReady = Buku.objects.filter(is_ready = True)
    dataPinjam = PeminjamanBuku.objects.filter(user=request.user, is_dikembalikan = False)
    context = {
        'dataReady': dataReady,
        'dataPinjam': dataPinjam
    }

    return render(request, 'pinjam.html', context)

@csrf_exempt
def pinjam_buku(request):
    if request.method == 'POST':
        formData = request.POST
        name = formData.get('namaUser')
        tanggal_akhir = formData.get('tanggalAkhir')
        tanggal_akhir_fix = datetime.strptime(tanggal_akhir, "%Y-%m-%d").date()
        bookId = formData.get('bookId')
        bukus = Buku.objects.filter(id=bookId)
        if (bukus.exists):
            for book in bukus:
                gambar = book.img
                book.is_ready = False;
                book.save()

        user = request.user

        new_peminjaman = PeminjamanBuku.objects.create(
            gambarBuku = gambar,
            user=user, 
            buku=bukus.first(), 
            nama=name, 
            tanggal_pengembalian= tanggal_akhir_fix, 
            is_dikembalikan = False,
        )
        new_peminjaman.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

def get_pinjam_json(request):
    dataPinjam = PeminjamanBuku.objects.filter(user=request.user).filter(is_dikembalikan=False)
    return HttpResponse(serializers.serialize('json', dataPinjam))

def get_buku_json(request):
    dataReady = Buku.objects.filter(is_ready = True)
    return HttpResponse(serializers.serialize('json', dataReady))

def get_buku_by_id(request, id):
    bukuDicari = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', bukuDicari))
