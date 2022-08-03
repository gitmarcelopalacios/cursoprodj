from django.contrib import admin
from .models import Departamento
# Register your models here.

#decoradores
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name',
        'shor_name',
    )

admin.site.register(Departamento, DepartamentoAdmin)

