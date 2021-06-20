from django.http import HttpResponse
from django.shortcuts import render
from .models import Transport, User
from django.views.generic import DetailView

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
class UserInfo(DetailView):
    model = User
    template_name = 'adm/user.html'
    context_object_name = 'user'

def users(request):
    user = User.objects.all()
    name = "Пользователb"
    return render(request, 'adm/users.html', {'user':user,'name':name})
