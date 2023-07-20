from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def editoriales(request):
    return render(request, 'editoriales.html')

def crear_editorial(request):
    return render(request, 'crear_editorial.html')

def paises(request):
    return render(request, 'paises.html')

def crear_pais(request):
    return render(request, 'crear_pais.html')
