import datetime
import json
from django.shortcuts import get_object_or_404, render
from .forms import ReservasiForm
from .models import Reservasi, TempatBaca
from buku.models import Buku
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
          # print(nama)
          no_hp = request.POST.get("no_hp")
          # print(no_hp)

          buku_id = request.POST.get("buku")
          buku = get_object_or_404(Buku, pk=buku_id)
          # print(buku)
          
          tempat_baca_id = request.POST.get("tempat_baca")
          tempat_baca = get_object_or_404(TempatBaca, pk=tempat_baca_id)
          print(tempat_baca)

          tanggal_str = request.POST.get("tanggal")
          tanggal = datetime.datetime.strptime(tanggal_str, "%Y-%m-%d").date()
          # print(tanggal)

          jam_str = request.POST.get("jam")
          jam = datetime.datetime.strptime(jam_str, "%H:%M").time()
          # print(jam)

          durasi_baca = request.POST.get("durasi_baca")
          # print(durasi_baca)
          user = request.user
          # print(user)

          buku.is_ready = False
          buku.save()

          tempat_baca.dipesan = True
          tempat_baca.save()

          new_reservasi = Reservasi(user=user, nama=nama, no_hp=no_hp, buku=buku, tempat_baca=tempat_baca, tanggal=tanggal, jam=jam, durasi_baca=durasi_baca)
          new_reservasi.save()
          print(new_reservasi)
          return HttpResponse(b"CREATED", status=201)
     else:
          return HttpResponseNotFound()

@csrf_exempt
def get_tempat_baca(request):
     tempat_baca = TempatBaca.objects.filter(dipesan = False)
     return HttpResponse(serializers.serialize('json', tempat_baca), content_type="application/json")

@csrf_exempt
def get_buku_json(request):
     daftar_buku = Buku.objects.filter(is_ready = True)
     return HttpResponse(serializers.serialize('json', daftar_buku), content_type="application/json")

def katalog(request):
     daftar_buku = Buku.objects.filter(is_ready = True)
     context = {'daftar_buku':daftar_buku}
     return render(request, 'katalog.html', context)

@csrf_exempt
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

@csrf_exempt
def get_reservasi_json_flutter(request):
     data = json.loads(request.body)

     user = get_object_or_404(User, username=data["user"])
     
     reservasi = Reservasi.objects.filter(user=user)
     return JsonResponse(serializers.serialize('json', reservasi))

@csrf_exempt
def selesai_flutter(request):
     if request.method == 'POST':
          data = json.loads(request.body)

          user = get_object_or_404(User, username=data["user"])
          reservasi_id = data["reservasi_id"]
          reservasi = Reservasi.objects.get(pk=reservasi_id, user=user)
          # buku = get_object_or_404(Buku, pk=int(data["buku"]))
          buku = reservasi.buku
          buku.is_ready = True
          buku.save()

          # tempat_baca = tempat_baca = get_object_or_404(TempatBaca, pk=int(data["tempat_baca"]))
          tempat_baca = reservasi.tempat_baca
          tempat_baca.dipesan = False 
          tempat_baca.save()

          reservasi.selesai = True
          reservasi.save()

          return JsonResponse({"status": "success"}, status=200)
     else:
          return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def create_reservasi_flutter(request):
     if request.method == 'POST':

          data = json.loads(request.body)
          # print(data)
          user= get_object_or_404(User, username=data["user"])
          # print(data["user"])

          buku = get_object_or_404(Buku, pk=int(data["buku"]))
          # if (buku.is_ready)
          buku.is_ready = False
          buku.save()

          tempat_baca = get_object_or_404(TempatBaca, pk=int(data["tempat_baca"]))
          tempat_baca.dipesan = True
          tempat_baca.save()

          new_reservasi = Reservasi.objects.create(
               user = user,
               nama = data["nama"],
               no_hp = data["no_hp"],
               buku = buku,
               tempat_baca = tempat_baca,
               tanggal = datetime.datetime.strptime(data["tanggal"], "%Y-%m-%d").date(),
               jam = datetime.datetime.strptime(data["jam"], "%H:%M").time(),
               durasi_baca = data["durasi_baca"],
          )

          new_reservasi.save()

          return JsonResponse({"status": "success"}, status=200)
     else:
          return JsonResponse({"status": "error"}, status=401)
# Create your views here.