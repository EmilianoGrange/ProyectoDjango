from django.http import HttpResponse
from datetime import datetime as d

def dia_de_hoy(req):
    dia = f"Hoy es: {d.now()}"
    return HttpResponse(dia)

def saludo_nombre(req, name):
    return HttpResponse(f"Hola, {name}")