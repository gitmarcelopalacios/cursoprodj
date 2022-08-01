from django.shortcuts import render

# Create your views here.

# importo la clase
from django.views.generic import TemplateView, ListView, DetailView, CreateView 

# importo el modelo
from .models import Empleado


class ListAllEmpleados(ListView):
    # listar todos los empleados de la empresa
    template_name = "persona/list_all.html"
    paginate_by = 4
    model = Empleado
    

class ListByAreaEmpleado(ListView):
    # listar todos los empleados que pertenecen a un area de la empresa
    template_name = "persona/list_by_area.html"

    def get_queryset(self):
        # aqui escribo el codigo que yo quiera
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
            )
        return lista 

class ListEmpleadosByKword(ListView):
    # listar los empleados por palabra clave
    template_name = "persona/by_kword.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
            )
        return lista

class ListHabilidadesEmpleados(ListView):
    # listar habilidades de un empleado
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context ['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    #fields = ['first_name','last_name','job']
    # muestra todos los campos
    fields = ('__all__')
    # recarga la misma pagina
    #success_url = '.'
    # redirecciono
    success_url = '/success'

