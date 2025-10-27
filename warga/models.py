from django.db import models

# Create your models here.
class warga(models.Model):
    nik = models.CharField(max_length=16, unique=True, verbose_name="Nomer Induk Kependudukan")
    nama_lengkap = models.CharField(max_length=100, verbose_name="Nama Lengkap")
    alamat = models.TextField(verbose_name="Alamat Tinggal")
    no_telpon = models.CharField(max_length=15, blank=True, verbose_name="Nomor Telpon")
    tanggal_registrasi = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nama_lengkap
    
class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU','Baru'),
        ('DIPROSES','Selesai'),
        ('SELESAI','Selesai'),
    ]
    
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BARU')
    tanggal_lapor = models.DateTimeField(auto_now_add=True)
    
    pelapor = models.ForeignKey(warga, on_delete=models.CASCADE, related_name='pengaduan')
    
    def __str__(self):
        return self.judul