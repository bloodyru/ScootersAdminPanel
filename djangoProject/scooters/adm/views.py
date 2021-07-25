from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Transport, User,Balance,Zone
from django.views.generic import DetailView
from .forms import UserForm,ZoneredactorForm
from django.views.generic.edit import UpdateView

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

def UserInfo(request, user_id):
    user = User.objects.get(pk=user_id)

    return render(request, 'adm/user.html',{'user':user})


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
    trans = Transport.objects.all()
    summtransport = Transport.objects.count()
    return render(request, 'adm/content/map.html', {'trans':trans,'name':name,'summtransport':summtransport})

def zone(request):
    name = "Зоны"
    zone = Zone.objects.all()
    summ = Zone.objects.count()
    n = summ % 10
    if n<=1:
        nn='зона'

    elif (n>=2 and n<=4):
        nn='зоны'
    elif (5<=n<=10):
        nn = 'зон'
    else:
        nn='зон.'

    return render(request, 'adm/zone.html', {'zone':zone,'name':name, 'summ':summ, 'nn':nn})


class Zoneredactor(UpdateView):
    model = Zone
    template_name_suffix = 'redactor'
    fields = ["Name", "TypeZone", "GPSPoints", "ColorZone"]

    # form_class = ZoneredactorForm
    # error = ''
    # if request.method == 'POST':
    #     form = ZoneredactorForm(request.POST)
    #     print("form21345678765432", form)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         error = form.errors
    #         print("error12345678765432",form)
    # zone = Zone.objects.get(pk=zone_id)
    # form = ZoneredactorForm(initial={'Name': zone.Name,
    #                                  'TypeZone': zone.TypeZone,
    #                                  'GPSPoints': zone.GPSPoints,
    #                                  'ColorZone': zone.ColorZone})
    # name = "Редактор зон"
    # # return HttpResponse(f"pfy htlfrnjh {zone} {zone_id}")
    # return render(request, 'adm/zoneredactor.html', {'name':name,'zone':zone, 'form':form, 'error':error})
