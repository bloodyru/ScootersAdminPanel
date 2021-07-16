from django.urls import path

from . import views

urlpatterns = [
    path('', views.transport, name='transport'),
    path('transport.html', views.transport, name='transport'),
    path('trips.html', views.trips, name='trips'),
    path('users.html', views.users, name='users'),
    path('user/<int:user_id>/$', views.UserInfo, name='user'),
    path('map.html', views.map, name='map'),
    path('zone.html', views.zone, name='zone'),
    path('zoneredactor/<int:pk>', views.Zoneredactor.as_view(), name='zoneredactor'),
]