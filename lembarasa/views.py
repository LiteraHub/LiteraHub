from django.shortcuts import render
from buku.models import Buku
from lembarasa.models import MyBuku
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import datetime
from lembarasa.forms import BukuForm, MyBukuForm

@login_required(login_url='/login')
def show_lembarasa(request):
    buku = Buku.objects.all()
    mybuku = MyBuku.objects.all()
    form_buku = BukuForm(request.POST or None)
    form_mybuku = MyBukuForm(request.POST or None)

    context = {
        'buku' : buku,
        'mybuku' : mybuku,
        'nama_user' : request.user.username,
        'form_buku' : form_buku,
        'form_mybuku' : form_mybuku,
    }

    return render(request, "lembarasa.html", context)

def show_json_buku(request):
    buku = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", buku), content_type="application/json")

def show_json_mybuku(request):
    my_buku = MyBuku.objects.all()
    return HttpResponse(serializers.serialize("json", my_buku), content_type="application/json")

def get_buku_json(request):
    list_id_buku = MyBuku.objects.filter(user=request.user).values_list('buku') #list_idbuku
    buku = Buku.objects.filter(id__in=list_id_buku)
    return HttpResponse(serializers.serialize('json', buku))

def get_mybuku_json_id(request,id):
    buku_cari = Buku.objects.get(pk=id)    
    mybuku = MyBuku.objects.get(buku = buku_cari)
    mybuku_list = [mybuku]
    return HttpResponse(serializers.serialize('json', mybuku_list))

@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        img = request.POST.get("img")
        isi = request.POST.get("isi")
        user = request.user
        year = datetime.datetime.today().year

        new_buku = Buku(isbn=0, title=title, author=user, year=year, img=img)
        new_buku.save()
        new_mybuku = MyBuku(buku=new_buku, user=user, isi=isi)
        new_mybuku.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_ajax(request, id):
    buku_delete = Buku.objects.get(pk = id)
    mybuku = MyBuku.objects.get(buku = buku_delete)
    mybuku.delete()
    buku_delete.delete()
    return HttpResponse(b"DELETED", status=201)