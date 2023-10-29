from django.forms import ModelForm
from django import forms
from peminjamanbuku.models import PeminjamanBuku 

class PinjamForm(ModelForm):
    nama = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w-full p-2 rounded border'}),
        label='Nama'
    )

    tanggal_pengembalian = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'w-full p-2 rounded border', 'type': 'date'}),
        label='Tanggal Pengembalian'
    )
    class Meta:
        model = PeminjamanBuku
        fields = ["nama","tanggal_pengembalian"]