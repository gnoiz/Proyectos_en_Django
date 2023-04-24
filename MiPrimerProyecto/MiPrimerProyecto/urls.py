"""MiPrimerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from MiPrimerProyecto.views import saludo, despedida, dame_el_dia, calcula_edad, saludo_Tere, EjemploA, EjemploB

urlpatterns = [
    path('admin/', admin.site.urls), #esta viene por defecto
    path('saludo/', saludo),        ##acá asignamos el nombre de la url por ejemplo: http://127.0.0.1:8000/saludo/
    path('sevemo/', despedida),     #acá asignamos el nombre de la url por ejemplo: http://127.0.0.1:8000/sevemo/
    path('fecha/', dame_el_dia),     #acá asignamos el nombre de la url por ejemplo: http://127.0.0.1:8000/fecha/
    path('futura/<int:edad>/<int:agno>', calcula_edad),     #acá asignamos el nombre de la url por ejemplo: http://127.0.0.1:8000/futura/"Introducir el año a calcular en INT", por ejemplo: http://127.0.0.1:8000/futura/2050
    path('tere/', saludo_Tere),     #acá asignamos el nombre de la url por ejemplo: http://127.0.0.1:8000/tere/
    path('EjemploA/', EjemploA),     #acá asignamos el nombre de la url por ejemplo: http://127.0.0.1:8000/EjemploA/
    path('EjemploB/', EjemploB),     #acá asignamos el nombre de la url por ejemplo: http://127.0.0.1:8000/EjemploB/
]
