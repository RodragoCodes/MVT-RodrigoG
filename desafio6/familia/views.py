


from django.shortcuts import render
from django.http import HttpResponse
from familia.models import familiares
# Create your views here.

def lista_familia(request):

    variable= familiares.objects.all()
    lista_nombres = []
    lista_edad = []
    lista_naci = []
    lista_DNI = []

    for i in variable: 
        lista_nombres.append(i.nombre)
    
    for a in variable:
        lista_edad.append(a.edad)
    
    for b in variable:
        lista_naci.append(b.nacimiento)
    
    for c in variable:
        lista_DNI.append(c.DNI)

    return HttpResponse(lista_nombres)


    
   
