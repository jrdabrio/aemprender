from django.contrib import admin
from web.models import Colegio, Alumno


@admin.register(Colegio)
class ColegioAdmin(admin.ModelAdmin):
    pass


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass
