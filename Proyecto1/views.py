from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime as d

def saludo(req):
    return HttpResponse("Hola Django-Coder")

def dia_de_hoy(req):
    dia = f"Hoy es: {d.now()}"
    return HttpResponse(dia)

def saludo_nombre(req, name):
    return HttpResponse(f"Hola, {name}")

def home_template(req):
    miHtml = open('Proyecto1/templates/home.html')

    plantilla = Template(miHtml.read())

    miHtml.close()

    context = Context()

    doc = plantilla.render(context)

    return HttpResponse(doc)