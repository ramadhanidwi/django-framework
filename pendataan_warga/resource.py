from import_export import resources
from pendataan_warga.models import data_warga
from import_export.fields import Field


class WargaResource(resources.ModelResource):
    tempat_tanggal_lahir = Field(attribute='tempat_tanggal_lahir', column_name="Tempat Tanggal Lahir")
    jenis_kelamin__nama = Field(attribute='jenis_kelamin', column_name="Jenis Kelamin")
    agama__nama = Field(attribute='agama', column_name='Agama')
    status_bantuan__nama = Field(attribute='status_bantuan', column_name="Status Bantuan")
    tanggal_upload = Field(attribute='tanggal_upload', column_name="Tanggal Upload")
    class Meta:
        model = data_warga
        fields=['nama','nik','tempat_tanggal_lahir','jenis_kelamin__nama','alamat','agama__nama','pekerjaan','status_bantuan__nama','tanggal_upload']
        export_order = ['nama','nik','tempat_tanggal_lahir','jenis_kelamin__nama','alamat','agama__nama','pekerjaan','status_bantuan__nama','tanggal_upload']
