from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserRegisterForm
from .models import Doctor, Medicina

# Create your views here.


def index(request):
    #medicina = Medicina.objects.all()
    #context = {'medicina': medicina, 'title': 'Поликлиника'}
    return render(request, 'mainApp/index.html')


def doctors(request):
    doctor = Doctor.objects.all()
    med = {
        'nevrop':Medicina.objects.get(name='Невропатология'),
        'androl':Medicina.objects.get(name='Андрология'),
        'aneste':Medicina.objects.get(name='Анестезиология'),
        'venero':Medicina.objects.get(name='Венерология'),
        'gastro':Medicina.objects.get(name='Гастроэнтерология'),
        'gineko':Medicina.objects.get(name='Гинекология'),
        'kardio':Medicina.objects.get(name='Кардиология'),
        'logope':Medicina.objects.get(name='Логопедия'),
        'mammol':Medicina.objects.get(name='Маммология'),
        'nevrol':Medicina.objects.get(name='Неврология'),
        'neuroh':Medicina.objects.get(name='Нейрохирургия'),
        'otolor':Medicina.objects.get(name='Отоларингология'),
        'oftalm':Medicina.objects.get(name='Офтальмология'),
        'pediat':Medicina.objects.get(name='Педиатрия'),
        'prokto':Medicina.objects.get(name='Проктология'),
        'terapi':Medicina.objects.get(name='Терапия'),
        'urolog':Medicina.objects.get(name='Урология'),
        'hirurg':Medicina.objects.get(name='Хирургия'),
        'endokr':Medicina.objects.get(name='Эндокринология')
    }
    context = {
        'title':'Врачи',
        'doc_androl' : Doctor.objects.filter(medicina=med['androl']),
        'doc_aneste' : Doctor.objects.filter(medicina=med['aneste']),
        'doc_venero' : Doctor.objects.filter(medicina=med['venero']),
        'doc_gastro' : Doctor.objects.filter(medicina=med['gastro']),
        'doc_gineko' : Doctor.objects.filter(medicina=med['gineko']),
        'doc_kardio' : Doctor.objects.filter(medicina=med['kardio']),
        'doc_logope' : Doctor.objects.filter(medicina=med['logope']),
        'doc_mammol' : Doctor.objects.filter(medicina=med['mammol']),
        'doc_nevrol' : Doctor.objects.filter(medicina=med['nevrol']),
        'doc_neuroh' : Doctor.objects.filter(medicina=med['neuroh']),
        'doc_otolor' : Doctor.objects.filter(medicina=med['otolor']),
        'doc_oftalm' : Doctor.objects.filter(medicina=med['oftalm']),
        'doc_pediat' : Doctor.objects.filter(medicina=med['pediat']),
        'doc_prokto' : Doctor.objects.filter(medicina=med['prokto']),
        'doc_terapi' : Doctor.objects.filter(medicina=med['terapi']),
        'doc_urolog' : Doctor.objects.filter(medicina=med['urolog']),
        'doc_hirurg' : Doctor.objects.filter(medicina=med['hirurg']),
        'doc_endokr' : Doctor.objects.filter(medicina=med['endokr'])
    }
    return render(request, 'mainApp/doctors.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Акканут создан для {username}!')
            return redirect("/login")
    else:
        form = UserRegisterForm()
        return render(request, 'registration/registration.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile.html')
    else:
        return redirect("/login")


def profile_data(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile_data.html')
    else:
        return redirect("/login")


def profile_patient(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile_patient.html')
    else:
        return redirect("/login")


def profile_medcard(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile_patient_card.html')
    else:
        return redirect("/login")


def profile_analyse(request):
    if request.user.is_authenticated:
        analyse = request.user.patient.out_patient_card.analyse.all()
        return render(request, 'profile/profile_analyse.html', {'analyse': analyse})
    else:
        return redirect("/login")


def test(request):
    return render(request, 'test.html')
