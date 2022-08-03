from django.contrib import admin
from .models import Prueba
from applications.home import forms

#decoradores
class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'titulo', 
        'subtitulo',
        'cantidad',
    )

admin.site.register(Prueba, HomeAdmin)