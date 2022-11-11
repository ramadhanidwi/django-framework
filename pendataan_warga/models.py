from django.db import models


#Create your models here.
class RukunTtg(models.Model):
    nama = models.CharField(max_length=2)
    def __str__(self):
        return self.nama

class JenisKelamin(models.Model):
    nama = models.CharField(max_length= 10)
    def __str__(self):
        return self.nama

class Agama(models.Model):
    nama = models.CharField(max_length=10)
    def __str__(self):
        return self.nama

class StatusBantuan(models.Model):
    nama = models.CharField(max_length=10)
    def __str__(self):
        return self.nama


class data_warga(models.Model):
    nama = models.CharField(max_length= 100)
    nik = models.CharField(max_length=  20)
    tempat_tanggal_lahir = models.CharField(max_length= 100)
    jenis_kelamin = models.ForeignKey(JenisKelamin, on_delete= models.CASCADE, null= True)
    alamat = models.CharField(max_length= 100)
    rt = models.ForeignKey(RukunTtg, on_delete= models.CASCADE, null= True)
    agama = models.ForeignKey(Agama, on_delete= models.CASCADE, null= True)
    pekerjaan = models.CharField(max_length= 100)
    status_bantuan = models.ForeignKey(StatusBantuan, on_delete= models.CASCADE, null= True)
    gambar = models.ImageField(upload_to= 'gambar/', null = True)
    tanggal_upload = models.DateTimeField(auto_now_add = True, null= True)

    def __str__(self):
        return self.nama