from django.http import HttpResponse
from django.shortcuts import render
from .models import Transport, User,Balance
from django.views.generic import DetailView
from .forms import UserForm

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
    error =  ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = form.errors

    user = User.objects.all()
    name = "Пользователи"
    form = UserForm()
    data = {
        'form': form,
        'user': user,
        'name': name,
        'error':error
    }


    return render(request, 'adm/users.html', data)
def map(request):
    name = "Карта"
    return render(request, 'adm/content/map.html', {'name':name})
