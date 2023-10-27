from django.forms import ModelForm
from .models import Reservasi

class ReservasiForm(ModelForm):
     class Meta:
          model = Reservasi
          fields = ['nama', 'no_hp', 'buku', 'tempat_baca', 'durasi_baca']