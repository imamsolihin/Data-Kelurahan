from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import warga, Pengaduan   # tambahkan Pengaduan di sini

# View untuk daftar warga
class WargaListView(ListView):
    model = warga
    template_name = 'warga_list.html'  # opsional, defaultnya otomatis

# View untuk detail warga
class WargaDetailView(DetailView):
    model = warga
    template_name = 'warga/warga_detail.html'  # opsional juga

# View baru untuk daftar semua pengaduan
class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'pengaduan_list.html'  # pastikan nanti kamu buat file ini di templates
    context_object_name = 'pengaduan_list'  # agar mudah dipanggil di template
