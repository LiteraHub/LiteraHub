from django.shortcuts import get_object_or_404, render, redirect
from .forms import ReservasiForm
from .models import Reservasi
from buku.models import Buku
from django.http import HttpResponse, JsonResponse
from django.core import serializers


def show_page_reservasi(request):
     context = {}
     return render(request, "main_reservasi.html", context)

def buat_reservasi(request):
     if request.method == 'POST':
          form = ReservasiForm(request.POST)
          if form.is_valid():
               reservasi_dibuat = form.save()
               return redirect('reservasi:receipt', reservasi_dibuat.id)
     else:
          form = ReservasiForm(initial={'buku': request.GET.get('buku_id')})
     context = {'form': form}
     return render(request, "buat_reservasi.html", context)
          
     
def receipt(request, reservasi_id):
     reservasi = get_object_or_404(Reservasi, id=reservasi_id)
     context = {'reservasi': reservasi}
     return render(request, 'receipt.html', context)

def get_buku_json(request):
     daftar_buku = Buku.objects.all()
     buku_data = [{"id": buku.id, "title": buku.title, "author": buku.author, "img": buku.img.url} for buku in daftar_buku]
     return JsonResponse(buku_data, safe=False)

# Create your views here.
