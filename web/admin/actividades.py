from django.contrib import admin
from web.models import (
    ActividadUno,
    RespuestasUno,
    ActividadDos,
    RespuestasDos,
    ActividadCuatro,
    RespuestasCuatro,
    ActividadCinco,
    RespuestasCinco,
    ActividadSeis,
    RespuestasSeis
)


@admin.register(ActividadUno)
class ActividadUnoAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(RespuestasUno)
class RespuestasUnoAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'actividad', 'valor']


@admin.register(ActividadDos)
class ActividadDosAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(RespuestasDos)
class RespuestasDosAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'valor']


@admin.register(ActividadCuatro)
class ActividadCuatroAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(RespuestasCuatro)
class RespuestasCuatroAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'valor']


@admin.register(ActividadCinco)
class ActividadCincoAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(RespuestasCinco)
class RespuestasCincoAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'valor']


@admin.register(ActividadSeis)
class ActividadSeisAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(RespuestasSeis)
class RespuestasSeisAdmin(admin.ModelAdmin):
    list_display = ['alumno', ]
