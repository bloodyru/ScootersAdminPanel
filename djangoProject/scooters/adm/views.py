from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'adm/index.html')
def transport(request):
    return render(request, 'adm/transport.html')