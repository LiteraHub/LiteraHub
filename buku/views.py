from django.shortcuts import render
from django.http import HttpResponse 
from django.core import serializers

from buku.models import Buku

def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")