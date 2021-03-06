from django.template import Template,Context, loader
from django.http import HttpResponse
from django.shortcuts import render
import os 

def hello_check(request):
    return HttpResponse("v0.0.0")

from app1.models import Curso

def nombre(self,nombre):
    texto = f"PROJECT_NAME: {nombre}"

    return HttpResponse(texto)


def renderTemplate(self):

    base_path = os.getcwd()
    template_folder = os.path.join(base_path,"portfolio/templates")
    print(template_folder)

    # Abrimos el archivo de la plantilla
    file = open(f"{template_folder}/template1.html".replace("\\","/"))

    # Cargamos plantilla
    template = Template(file.read())

    # Cerramos el archivo
    file.close()

    diccionarioContexto = {
        "nombre":"Projecto Django",
        "nombres":["Felipe","Camila","Sharon","Diana","Juana"]
    }

    contexto = Context(diccionarioContexto)

    plantilla = template.render(contexto)

    return HttpResponse(plantilla)


def loader_template(slef):
    plantilla = loader.get_template("template1.html")

    diccionarioContexto = {
        "nombre":"Projecto Django2",
        "nombres":["Felipe2","A","B","C","D"]
    }
    documento = plantilla.render(diccionarioContexto)
    return HttpResponse(documento)


def guardar_curso(self,nombre,camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse(curso)
