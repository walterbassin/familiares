from django.shortcuts import render
from django.http import HttpResponse

from familiares.models import familiares

# Create your views here.
def listado_familiares (request):
    familiar= familiares.objects.all()
    context={'familiar': familiar}
    return render (request, 'familiares.html', context=context)

def web_familiares (request):
    return HttpResponse('<h2> Felicitaciones! Estás en una web que contiene una base de datos de tus familiares ;-) <h2>')