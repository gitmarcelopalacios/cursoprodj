from django.contrib import admin
from django.urls import path
# importo la vista
from . import views
urlpatterns = [
    path(
        'home/', 
        views.IndexView.as_view()
    ),
    path(
        'lista/', 
        views.PruebaListView.as_view()
    ),
    path(
        'add-prueba/', 
        views.PruebaCreateView.as_view(), 
        name='prueba_add'
    ),
    path(
        'lista-prueba/',
        views.ModeloPruebaListView.as_view()
    ),
]
