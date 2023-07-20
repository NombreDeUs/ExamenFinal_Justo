"""
URL configuration for ExamenFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from miapp import views


urlpatterns = [
    path('', views.inicio, name='inicio'),


    path('editoriales/', views.listar_editoriales, name='editoriales'),
    path('crear_editorial/', views.crear_editorial, name='crear_editorial'),
    path('eliminar_editorial/<int:carrera_id>/', views.eliminar_editorial, name='eliminar_editorial'),
    path('editar_editorial/<int:carrera_id>/', views.editar_editorial, name='editar_editorial'),  # Verifica esta línea

    path('paises/', views.listar_paises, name='paises'),
    path('crear_pais/', views.crear_pais, name='crear_pais'),
    path('eliminar_pais/<int:idcurso>/', views.eliminar_pais, name='eliminar_pais'),
    path('modificar_pais/<int:idcurso>/', views.modificar_pais, name='modificar_pais'),

]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


