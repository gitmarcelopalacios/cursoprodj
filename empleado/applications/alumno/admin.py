from django.contrib import admin
from .models import Alumno

# Register your models here.

#decoradores
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombres', 
        'dni',
        'telefono',
        'correo_electronico',
        'curso'
    )
    ordering = ['correo_electronico']
    search_fields = ('nombres','correo_electronico','dni')
    list_filter = ['curso',]

admin.site.register(Alumno, AlumnoAdmin)
