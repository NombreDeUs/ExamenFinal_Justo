from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def paises(request):
    return render(request, 'paises.html')

def crear_pais(request):
    return render(request, 'crear_pais.html')

#def carreras(request):
 #   return render(request, 'carreras.html')

#def crear_carrera(request):
 #   return render(request, 'crear_carrera.html')

# mi_aplicacion/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Career

def listar_editoriales(request):
    editoriales = Career.objects.all()
    return render(request, 'editoriales.html', {'editoriales': editoriales})

def crear_editorial(request):
    if request.method == 'POST':
        name = request.POST['name']
        shortname = request.POST['shortname']
        image = request.FILES.get('image')  # Usa request.FILES para obtener la imagen enviada

        # Obtenemos el valor del campo state como un string ('on' o None)
        state_str = request.POST.get('state', None)

        # Convertimos el string a un valor booleano válido (True o False)
        state = True if state_str == 'on' else False

        Career.objects.create(name=name, shortname=shortname, image=image, state=state)
        messages.success(request, 'Carrera agregada exitosamente.')
        return redirect('editoriales')

    return render(request, 'crear_editorial.html')

def eliminar_editorial(request, carrera_id):
    editorial = get_object_or_404(Career, idcareer=carrera_id)
    editorial.delete()
    messages.success(request, 'Carrera eliminada exitosamente.')
    return redirect('editoriales')

def editar_editorial(request, carrera_id):
    editorial = get_object_or_404(Career, idcareer=carrera_id)
    if request.method == 'POST':
        if 'name' in request.POST:
            editorial.name = request.POST['name']
        if 'shortname' in request.POST:
            editorial.shortname = request.POST['shortname']
        if 'image' in request.FILES:
            editorial.image = request.FILES['image']
        if 'state' in request.POST:
            editorial.state = request.POST.get('state') == 'on'
        editorial.save()
        messages.success(request, 'Carrera actualizada exitosamente.')
        return redirect('editoriales')

    return render(request, 'editar_editorial.html', {'editorial': editorial})