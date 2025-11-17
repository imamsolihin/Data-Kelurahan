# warga/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

# Buat router
router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')        # TAMBAH basename
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')  # TAMBAH basename

# URL patterns otomatis dari router
urlpatterns = [
    path('', include(router.urls)),
]