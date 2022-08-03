from unicodedata import name
from django.contrib import admin

from django.urls import path

from applications.departamento.views import NewDepartamentoView

from . import views

# importo la vista
urlpatterns = [
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='nuevo_departamento'),

]
