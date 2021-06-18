from django.urls import path

from . import views

urlpatterns = [
    path('', views.transport, name='transport'),
    path('transport.html', views.transport, name='transport'),
    path('trips.html', views.trips, name='trips'),
    path('users.html', views.users, name='users'),
    path('user.html', views.user, name='user'),
]