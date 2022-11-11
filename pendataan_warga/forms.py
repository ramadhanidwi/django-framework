from django import forms
from django.forms import ModelForm
from pendataan_warga.models import data_warga

class FormWarga(ModelForm):
    class Meta:
        model = data_warga
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class':'form-control'}),
            'nik': forms.TextInput({'class':'form-control'}),
            'tempat_tanggal_lahir': forms.TextInput({'class':'form-control'}),
            'jenis_kelamin': forms.Select({'class':'form-control'}),
            'alamat': forms.TextInput({'class':'form-control'}),
            'rt': forms.Select({'class':'form-control'}),
            'agama': forms.Select({'class':'form-control'}),
            'pekerjaan': forms.TextInput({'class':'form-control'}),
            'status_bantuan': forms.Select({'class':'form-control'}),
        }