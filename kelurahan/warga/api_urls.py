from django.urls import path
from .views import (
    WargaListAPIView, 
    WargaDetailAPIView,
    PengaduanListAPIView, 
    PengaduanDetailAPIView
)

urlpatterns = [
    # Endpoints untuk Warga
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
    
    # Endpoints untuk Pengaduan
    path('pengaduan/', PengaduanListAPIView.as_view(), name='api-pengaduan-list'),
    path('pengaduan/<int:pk>/', PengaduanDetailAPIView.as_view(), name='api-pengaduan-detail'),
]