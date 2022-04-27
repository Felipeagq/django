from django.http import HttpResponse

def hello_check(request):
    return HttpResponse("v0.0.0")