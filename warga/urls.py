from django.urls import path
from .views import WargaListView, WargaDetailView, PengaduanListView   # <-- tambahkan WargaDetailView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga_list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
]
