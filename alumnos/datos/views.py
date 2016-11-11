from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return render(request, "index.html", {"nombre": "Carlinne Pacheco"})
# Create your views here.

def formulario(request):
    form = "Hola este es mi formulario"
    return render(request, "formulario.html", {"formulario": form})
