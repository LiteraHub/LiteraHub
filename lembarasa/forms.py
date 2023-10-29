from django.forms import ModelForm
from lembarasa.models import MyBuku
from buku.models import Buku

class BukuForm(ModelForm):
    class Meta:
        model = Buku
        fields = ["title", "img"]

class MyBukuForm(ModelForm):
    class Meta:
        model = MyBuku
        fields = ["isi"]