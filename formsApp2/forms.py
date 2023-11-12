from django import forms
from formsApp2.models import Preguntas
from django.core import validators

class FormProyecto(forms.ModelForm):
    
    nombre = forms.CharField(min_length=2,max_length=15)

    class Meta:
        model = Preguntas
        fields = '__all__'

    