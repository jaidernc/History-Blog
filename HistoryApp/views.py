from django.shortcuts import render
from HistoryApp.models import*
from django.http import HttpResponse
# Create your views here.
def tema(self):

    tema = Temas(nombre='Imperio Egipcio', categoria='Historia Antigua')
    tema.save()

    documentDeTexto= f'-----> nombre: {tema.nombre}, categoria: {tema.categoria}'

    return HttpResponse(documentDeTexto)
