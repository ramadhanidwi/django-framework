from django.contrib import admin
from pendataan_warga.models import *


class DataAdmin(admin.ModelAdmin):
    list_display = ['nama','nik','tempat_tanggal_lahir','jenis_kelamin','alamat','rt','agama','pekerjaan','status_bantuan']
    list_fields = ['nama','nik','tempat_tanggal_lahir','jenis_kelamin','alamat','rt','agama','pekerjaan','status_bantuan']
    list_filter = ('rt','agama','status_bantuan')
    list_per_page = 4
# Register your models here.
admin.site.register(data_warga, DataAdmin)
admin.site.register(StatusBantuan)
admin.site.register(Agama)
admin.site.register(JenisKelamin)
admin.site.register(RukunTtg)