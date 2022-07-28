from django.contrib import admin
from django.urls import path
# importo la vista
from . import views
urlpatterns = [
    path('home/', views.IndexView.as_view()),
]
