from django.contrib import admin
from django.urls import path
from pendataan_warga.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('data/', data_rakyat, name='data_rakyat'),
    path('tambah-warga/', tambah_warga, name='tambah_warga'),
    path('data/hapus/<int:id_data_rakyat>', hapus_data, name='hapus_data'),
    path('data/ubah/<int:id_data_rakyat>', ubah_warga, name= 'ubah'),
    path('masuk/', LoginView.as_view(), name = 'masuk'),
    path('keluar/', LogoutView.as_view(next_page= 'masuk'), name='keluar'),
    path('signup/', signup, name='signup'),
    path('export/xls' , export_xls, name='export_excel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)