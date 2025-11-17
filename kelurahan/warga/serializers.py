from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon', 'tanggal_registrasi']
        # SESUAIKAN DENGAN MODEL WARGA ANDA

class PengaduanSerializer(serializers.ModelSerializer):
    # Sesuaikan dengan field yang ada di model Pengaduan
    nama_pelapor = serializers.CharField(source='pelapor.nama_lengkap', read_only=True)
    
    class Meta:
        model = Pengaduan
        fields = ['id', 'pelapor', 'nama_pelapor', 'judul', 'deskripsi', 'status', 'tanggal_lapor']
        # SESUAIKAN DENGAN MODEL PENGADUAN ANDA