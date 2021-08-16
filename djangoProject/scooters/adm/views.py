from django.core import serializers
# from django.utils import simplejson
from django.core.management.commands import dumpdata
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Transport, User, Balance, Zone
from django.views.generic import DetailView
from .forms import UserForm, ZoneredactorForm, NewZoneForm
from django.views.generic.edit import UpdateView, CreateView
import json


def index(request):
    return render(request, 'adm/index.html')


def transport(request):
    name = "Транспорт"
    trans = Transport.objects.all()
    return render(request, 'adm/transport.html', {'trans': trans, 'name': name})


def trips(request):
    name = "Поездки"
    user = User.objects.all()
    return render(request, 'adm/trips.html', {'user': user, 'name': name})


def UserInfo(request, user_id):
    user = User.objects.get(pk=user_id)

    return render(request, 'adm/user.html', {'user': user})


def users(request):
    error = ''
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
        'error': error
    }
    return render(request, 'adm/users.html', data)


def map(request):
    name = "Карта"
    trans = Transport.objects.all()
    summtransport = Transport.objects.count()
    return render(request, 'adm/content/map.html', {'trans': trans, 'name': name, 'summtransport': summtransport})


def zone(request):
    name = "Зоны"
    zone = Zone.objects.all()
    colorZone = serializers.serialize('json', Zone.objects.all())
    color = json.loads(colorZone)  # конвертируем json to array
    datacolor = []
    for i in range(len(color)):
        color0 = color[i]  # берем первую строчку матрицы
        color0 = color0['fields']  # берем параметр fields, углубляемся
        color0 = color0['ColorZone']  # Берем параметр GPSPoints, получаем строчку
        datacolor.append(color0)
    data = serializers.serialize('json', Zone.objects.all())
    gps = json.loads(data)  # конвертируем json to array
    datagps = []
    for i in range(len(gps)):
        gps0 = gps[i]  # берем первую строчку матрицы
        gps0 = gps0['fields']  # берем параметр fields, углубляемся
        gps0 = gps0['GPSPoints']  # Берем параметр GPSPoints, получаем строчку
        datagps.append(gps0)
    summ = Zone.objects.count()
    n = summ % 10
    if n <= 1:
        nn = 'зона'

    elif (n >= 2 and n <= 4):
        nn = 'зоны'
    elif (5 <= n <= 10):
        nn = 'зон'
    else:
        nn = 'зон.'

    return render(request, 'adm/zone.html',
                  {'zone': zone, 'name': name, 'summ': summ, 'nn': nn, 'datagps': datagps, 'datacolor': datacolor})


class Zoneredactor(UpdateView):
    model = Zone
    template_name_suffix = 'redactor'
    fields = ["Name", "TypeZone", "GPSPoints", "ColorZone"]


class Newzone(CreateView):
    model = Zone
    template_name = 'adm/zonenew.html'
    fields = ["Name", "TypeZone", "GPSPoints", "ColorZone"]
    success_url = "zone.html"

    def get(self, request):
        name = "Добавление новой зоны"
        form = NewZoneForm()
        return render(request,self.template_name, { 'name': name, 'form': form})

def deletezone(request, pk):
    try:
        zone = Zone.objects.get(pk=pk)
        zone.delete()
        return HttpResponseRedirect('/zone.html')
    except zone.DoesNotExist:
        return HttpResponseNotFound("<h2>Zone not found</h2>")