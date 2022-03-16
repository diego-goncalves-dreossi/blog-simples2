import imp
from django.shortcuts import render
from .models import Artigo

# Create your views here.

def paginaInicial(request):
    artigos = Artigo.objects.all()
    return render(request,'home.html',{'artigos':artigos})

def verArtigo(request,artigo_id):
    artigo = Artigo.objects.get(pk=artigo_id)
    return render(request,'artigo.html',{'artigo':artigo})

