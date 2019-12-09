from django.urls import path

from .views import auth_views, actividades
from .home import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('actividad/uno/<int:pk>/', actividades.ActividadUnoView.as_view(), name='actividad-uno'),
    path('actividad/dos/', actividades.ActividadDosView.as_view(), name='actividad-dos'),
    path('actividad/tres/', actividades.ActividadTresView.as_view(), name='actividad-tres'),
    path('actividad/cuatro/', actividades.ActividadCuatroView.as_view(), name='actividad-cuatro'),
    path('actividad/cinco/', actividades.ActividadCincoView.as_view(), name='actividad-cinco'),
    path('actividad/seis/', actividades.ActividadSeisView.as_view(), name='actividad-seis'),
]
