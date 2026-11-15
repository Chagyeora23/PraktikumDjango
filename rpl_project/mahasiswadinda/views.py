from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Mahasiswa


def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswadinda/index.html', context)

# READ
@login_required(login_url='/accounts/login/')
def daftar(request):
    mahasiswa = Mahasiswa.objects.all()
    return render(request, 'mahasiswadinda/daftar.html', {'mahasiswa': mahasiswa})


# CREATE
@login_required(login_url='/accounts/login/')
def tambah_mahasiswa(request):
    if request.method == 'POST':
        Mahasiswa.objects.create(
            nim=request.POST.get('nim'),
            nama=request.POST.get('nama'),
            programstudi=request.POST.get('programstudi'),
        )
        return redirect('daftar')
    return render(request, 'mahasiswadinda/tambah.html')


# UPDATE
@login_required(login_url='/accounts/login/')
def edit_mahasiswa(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)
    if request.method == 'POST':
        mhs.nim = request.POST['nim']
        mhs.nama = request.POST['nama']
        mhs.programstudi = request.POST['programstudi']
        mhs.save()
        return redirect('daftar')
    return render(request, 'mahasiswadinda/edit.html', {'mhs': mhs})


# DELETE
@login_required(login_url='/accounts/login/')
@require_POST
def hapus_mahasiswa(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)
    mhs.delete()
    return redirect('daftar')