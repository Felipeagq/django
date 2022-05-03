from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    # return HttpResponse("vista de inicio")
    return render(request,"app1/inicio.html")


def cursos(request):
    return HttpResponse("vista de cursos")


def profesores(request):
    return HttpResponse("vista de profesores")


def estudiantes(request):
    return HttpResponse("vista de estudiantes")


def entregables(request):
    return HttpResponse("vista de entregables")

    