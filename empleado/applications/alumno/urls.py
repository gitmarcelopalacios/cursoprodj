from django.contrib import admin
from django.urls import path
# importo la vista
from . import views
urlpatterns = [
    path(
        'index/', 
        views.HomeView.as_view()
    ),
    path(
        'listar_alumnos/', 
        views.Listar_alumnos.as_view()
    ),
    path(
        'add-alumno/', 
        views.AlumnoCreateView.as_view()
    ),

]


