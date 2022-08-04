from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView

from .models import Prueba

from .forms import PruebaForm

# Create your views here.
class IndexView(TemplateView):
    template_name='home/home.html'

class ResumeFoundationView(TemplateView):
    template_name='home/resume_foundation.html'

class PruebaListView(ListView):
    template_name='home/lista.html'
    queryset = ['A','B','C'] 
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = 'lita_prueba'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'

class HomeTemplate1View(TemplateView):
    template_name='home/home1.html'

class HomeTemplate2View(TemplateView):
    template_name='home/home2.html'

class HomeTemplate3View(TemplateView):
    template_name='home/home3.html'
