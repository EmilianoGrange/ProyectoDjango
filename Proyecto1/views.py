from django.http import HttpResponse
from django.template import loader
from datetime import datetime as d

def saludo(req):
    return HttpResponse("Hola Django-Coder")

def dia_de_hoy(req):
    dia = f"Hoy es: {d.now()}"
    return HttpResponse(dia)

def saludo_nombre(req, name):
    return HttpResponse(f"Hola, {name}")

def home_template(req):

    user = {"name": "Emiliano", "last_name": "Grange", "list": [1,2,3,4,5]}

    plantilla = loader.get_template('home.html')

    doc = plantilla.render(user)

    return HttpResponse(doc)