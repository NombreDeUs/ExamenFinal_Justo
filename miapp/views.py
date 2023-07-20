from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

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

##----------------------------------------------------------

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from django.contrib import messages

def listar_paises(request):
    paises = Course.objects.all()
    return render(request, 'paises.html', {'paises': paises})

def crear_pais(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        code = request.POST['code']
        name = request.POST['name']
        hour = request.POST['hour']
        state = True if 'state' in request.POST else False

        # Crear y guardar el nuevo curso en la base de datos
        pais = Course(code=code, name=name, hour=hour, state=state)
        pais.save()

        # Mostrar mensaje de éxito
        messages.success(request, 'Pais agregado correctamente.')

        # Redireccionar a la lista de cursos
        return redirect('paises')

    return render(request, 'crear_pais.html')

def eliminar_pais(request, idcurso):
    pais = get_object_or_404(Course, idcourse=idcurso)
    pais.delete()
    messages.success(request, 'Pais eliminado exitosamente.')
    return redirect('paises')

def modificar_pais(request, idcurso):
    # Buscar el curso por su ID
    pais = get_object_or_404(Course, pk=idcurso)

    if request.method == 'POST':
        # Obtener datos del formulario enviado
        code = request.POST['code']
        name = request.POST['name']
        hour = request.POST['hour']
        state = True if 'state' in request.POST else False

        # Modificar los datos del curso
        pais.code = code
        pais.name = name
        pais.hour = hour
        pais.state = state
        pais.save()

        # Mostrar mensaje de éxito
        messages.success(request, 'Pais modificado correctamente.')

        # Redireccionar a la lista de cursos
        return redirect('paises')

    return render(request, 'modificar_pais.html', {'pais': pais})





