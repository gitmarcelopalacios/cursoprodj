from django.contrib import admin
from .models import Prueba

#decoradores
class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'titulo', 
        'subtitulo',
        'cantidad',
    )

admin.site.register(Prueba, HomeAdmin)