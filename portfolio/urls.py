"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from portfolio.views import hello_check,nombre, renderTemplate,loader_template,guardar_curso

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", hello_check),
    path("projectname/<nombre>",nombre),
    path("template1",renderTemplate),
    path("template2",loader_template),
    path("curso/<nombre>/<camada>",guardar_curso),

    path("app1/", include("app1.urls"))


]
