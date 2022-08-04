from django.contrib import admin
from django.urls import path
# importo la vista
from . import views
urlpatterns = [
   
    path(
        'prueba/', 
        views.IndexView.as_view()
    ),
   
    path(
        'resume-foundation/', 
        views.ResumeFoundationView.as_view(),
        name = 'resume_foundation_page'
    ),
   
    path(
        'home/', 
        views.IndexView.as_view(),
        name='home'
    ),

    path(
        'home1/', 
        views.HomeTemplate1View.as_view(),
        name='home1'
    ),
   
    path(
        'home2/', 
        views.HomeTemplate2View.as_view(),
        name='home2'
    ),
   
    path(
        'home3/', 
        views.HomeTemplate3View.as_view(),
        name='home3'
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
