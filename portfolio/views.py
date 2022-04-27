from django.http import HttpResponse

def hello_check(request):
    return HttpResponse("v0.0.0")


def nombre(self,nombre):
    texto = f"PROJECT_NAME: {nombre}"
    return HttpResponse(texto)