from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from django.core import serializers

from buku.models import Buku

def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def replace_img(request):
    data = Buku.objects.all()
    for buku in data:
        buku.img = buku.img.replace("http", "https").replace("images.", "m.media-")
        buku.save(update_fields=["img"])
    return JsonResponse({"status": "success"}, status=200)