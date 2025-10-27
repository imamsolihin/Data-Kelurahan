from django import forms
from .models import Warga, Pengaduan

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']


class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['pelapor', 'judul', 'deskripsi', 'status']  # ubah 'warga' → 'pelapor'

