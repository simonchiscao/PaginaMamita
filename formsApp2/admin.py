from django.contrib import admin
from .models import Preguntas

# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre','email','edad','respuestaOne']
    

admin.site.register(Preguntas, ProyectoAdmin)
