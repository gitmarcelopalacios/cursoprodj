from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Alumno."""

    class Meta:
        """Meta definition for Alumnoform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese texto aquí'
                }
            )
        }

    def clean_cantidad(self):
        # validacion por cantidad < 10
        cantidad = self.cleaned_data['cantidad']
        if cantidad<10:
            raise forms.ValidationError('Ingrese un número mayor a 10') 
        return cantidad