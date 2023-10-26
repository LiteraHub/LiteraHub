from django.shortcuts import render
from buku.models import Buku

# Create your views here.

def show_lembarasa(request):
    buku = Buku.objects.all()

    context = {
        'buku' : buku,
    }

    return render(request, "lembarasa.html", context)