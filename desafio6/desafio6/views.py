from django.apps import apps
from django.http import HttpResponse
from django.template import Template, Context



def index(request):
    
    datos_contexto= {"nombre": "Rodrigo", "edad": "29"}

    archivo = open(r"E:\Python_proyectos\Desafio6\desafio6\desafio6\Templates\Index.html", "r")
    contenido_html= archivo.read()
    archivo.close()

    plantilla = Template(contenido_html)

    contexto = Context(datos_contexto)

    render= plantilla.render(contexto)

    return HttpResponse(render)