from django.shortcuts import render, redirect, HttpResponse
from pendataan_warga.models import data_warga
from pendataan_warga.forms import FormWarga
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from pendataan_warga.resource import WargaResource



@login_required(login_url = settings.LOGIN_URL) 
def export_xls(request):
    data = WargaResource()
    dataset = data.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.mas-excel')
    response['Content-Disposition']= 'attachment; filename="Data warga.xls"'
    return response

@login_required(login_url = settings.LOGIN_URL)    
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pengguna Berhasil Dibuat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks={
            'form':form,
        }
    return render(request, 'signup.html', konteks)

@login_required(login_url = settings.LOGIN_URL)
def  home(request):
    template = 'home.html'
    return render(request, template)

@login_required(login_url = settings.LOGIN_URL)
def ubah_warga(request,id_data_rakyat):
    data = data_warga.objects.get(id = id_data_rakyat)
    template = 'ubah.html'
    if request.POST:
        form = FormWarga(request.POST, request.FILES, instance= data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah!")
            return redirect('ubah', id_data = id_data_rakyat)
    else:
        form = FormWarga(instance= data)
        konteks={
            'form':form,
            'data':data,
        }
    return render(request, template, konteks)

@login_required(login_url = settings.LOGIN_URL)    
def hapus_data(request, id_data_rakyat):
    data = data_warga.objects.filter(id = id_data_rakyat)
    data.delete()
    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('data_rakyat')

@login_required(login_url = settings.LOGIN_URL)
def data_rakyat(request):                   #sama kaya method buku
    if request.POST:
        kata_kunci = request.POST['pencarian']
        data = data_warga.objects.filter(nama__contains=kata_kunci)
        konteks = {
            'data': data,
        }
    else:
        data = data_warga.objects.all()
        konteks = {
            'data': data,
        }
    return render(request, 'data_warga.html', konteks)

@login_required(login_url = settings.LOGIN_URL)
def tambah_warga(request):
    if request.POST:
        form = FormWarga(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormWarga()
            pesan = "Data Berhasil Disimpan!!"
            konteks = {
                    'form': form,
                    'pesan': pesan,
            }
            return render (request, 'tambah_warga.html', konteks)
    else:
        form = FormWarga()
        konteks={
            'form' : form, 
        }
    return render(request, 'tambah_warga.html', konteks)