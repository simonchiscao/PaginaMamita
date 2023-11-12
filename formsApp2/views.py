from django.shortcuts import render, redirect
from formsApp2.forms import FormProyecto
from formsApp2.models import Preguntas
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoProyectos(request):
    preguntas = Preguntas.objects.all()
    data = {'preguntas' : preguntas}
    return render(request, 'historialReportes.html', data)

def agregarProyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentario ingresado exitosamente")
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarReporte.html', data)

def eliminarProyecto(request, id):
    proyecto = Preguntas.objects.get(id = id)
    proyecto.delete()
    messages.success(request, "Eliminación Exitosa")
    return redirect('/historialReportes')

def actualizarProyecto(request, id):
    proyecto = Preguntas.objects.get(id = id)
    form = FormProyecto(instance=proyecto)
    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentario Actualizado exitosamente")
        return index(request)
    data = { 'form' : form}
    return render(request, 'agregarReporte.html', data)

