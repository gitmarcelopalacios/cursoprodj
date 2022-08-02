from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Alumno
from django.urls import reverse_lazy
# Create your views here.
class HomeView(TemplateView):
    template_name='alumno/home.html'

class Listar_alumnos(ListView):
    # listar todos los alummnos
    template_name = "alumno/listar_alumnos.html"
    model = Alumno
    fields = (
        'nombres', 
        'dni',
        'telefono',
        'correo_electronico',
        'curso'
    )   

class AlumnoCreateView(CreateView):
    template_name = "alumno/add.html"
    model = Alumno
    fields = (
        'nombres', 
        'dni',
        'telefono',
        'correo_electronico',
        'curso'
    )   
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        # empleado = form.save(commit=False)
        # empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        # empleado.save()
        return super(AlumnoCreateView, self).form_valid(form)

    