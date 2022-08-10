from django import forms

from django import forms 

from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model=Empleado
        fields=(
            "",
            "",
            "",
            "",
            "",
            "",
        )