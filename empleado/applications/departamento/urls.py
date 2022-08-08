from unicodedata import name
from django.contrib import admin

from django.urls import path

from applications.departamento.views import NewDepartamentoView

from . import views

app_name = "departamento_app"

# importo la vista
urlpatterns = [
    
    path(
        'departamento-lista/', 
        views.DepartamentoListView.as_view(), 
        name='departamento_list'
    ),
    
    path(
        'new-departamento/', 
        views.NewDepartamentoView.as_view(), 
        name='nuevo_departamento'
    ),

]
