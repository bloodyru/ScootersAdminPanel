from django.http import HttpResponse
from django.shortcuts import render
from .models import Transport, User

def index(request):
    return render(request, 'adm/index.html')
def transport(request):
    name = "Транспорт"
    trans = Transport.objects.all()
    return render(request, 'adm/transport.html', {'trans':trans, 'name':name})
def trips(request):
    name = "Поездки"
    user = User.objects.all()
    return render(request, 'adm/trips.html', {'user':user,'name':name})
def users(request):
    user = User.objects.all()
    name = "Пользователи"
    return render(request, 'adm/users.html', {'user':user,'name':name})
def user(request):
    user = User.objects.all()
    name = "Пользователь"
    return render(request, 'adm/user.html', {'user':user,'name':name})
