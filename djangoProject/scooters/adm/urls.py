from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transport.html', views.transport, name='transport'),
]