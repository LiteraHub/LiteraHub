import datetime
from django.shortcuts import get_object_or_404, render
from .forms import ReservasiForm
from .models import Reservasi, TempatBaca
from buku.models import Buku
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_page_reservasi(request):
     reservasi = Reservasi.objects.filter(user=request.user)
     context = {
          'nama': request.user.username,
          'reservasi': reservasi
     }
     return render(request, "main_reservasi.html", context)

@csrf_exempt
def buat_reservasi(request):
     if request.method == 'POST':
          nama = request.POST.get("nama")
          no_hp = request.POST.get("no_hp")

          buku_id = request.POST.get("buku")
          buku = get_object_or_404(Buku, pk=buku_id)
          
          tempat_baca_id = request.POST.get("tempat_baca")
          tempat_baca = get_object_or_404(TempatBaca, pk=tempat_baca_id)

          tanggal_str = request.POST.get("tanggal")
          tanggal = datetime.datetime.strptime(tanggal_str, "%Y-%m-%d").date()

          jam_str = request.POST.get("jam")
          jam = datetime.datetime.strptime(jam_str, "%H:%M").time()

          durasi_baca = request.POST.get("durasi_baca")
          user = request.user

          buku.is_ready = False
          buku.save()

          tempat_baca.dipesan = True
          tempat_baca.save()

          new_reservasi = Reservasi(nama=nama, no_hp=no_hp, buku=buku, tempat_baca=tempat_baca, tanggal=tanggal, jam=jam, durasi_baca=durasi_baca, user=user)
          new_reservasi.save()

          return HttpResponse(b"CREATED", status=201)
    
     return HttpResponseNotFound()

def get_tempat_baca(request):
     tempat_baca = TempatBaca.objects.filter(dipesan = False)
     return HttpResponse(serializers.serialize('json', tempat_baca), content_type="application/json")

def get_buku_json(request):
     daftar_buku = Buku.objects.filter(is_ready = True)
     return HttpResponse(serializers.serialize('json', daftar_buku), content_type="application/json")

def katalog(request):
     daftar_buku = Buku.objects.filter(is_ready = True)
     context = {'daftar_buku':daftar_buku}
     return render(request, 'katalog.html', context)

def get_reservasi_json(request):
     reservasi = Reservasi.objects.filter(user=request.user)
     return HttpResponse(serializers.serialize('json', reservasi))

@csrf_exempt
def selesai(request, reservasi_id):
     if request.method == 'POST':
          user = request.user
          reservasi = Reservasi.objects.get(pk=reservasi_id, user=user)
          buku = reservasi.buku
          buku.is_ready = True
          buku.save()

          tempat_baca = reservasi.tempat_baca
          tempat_baca.dipesan = False 
          tempat_baca.save()

          reservasi.selesai = True
          reservasi.save()

          return HttpResponse(b"UPDATED", status=200)
     
     return HttpResponseNotFound()

# Create your views here.
