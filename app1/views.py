from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("vista de inicio")


def cursos(request):
    return HttpResponse("vista de cursos")


def profesores(request):
    return HttpResponse("vista de profesores")


def estudiantes(request):
    return HttpResponse("vista de estudiantes")


def entregables(request):
    return HttpResponse("vista de entregables")

    