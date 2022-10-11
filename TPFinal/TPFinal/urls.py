"""TPFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Cuentas.views import *
from Blog.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#Generales
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('about/', aboutMe, name="acercaDeMi"),
    path('notYet/', notYet, name="facebook"),
    path('notYet/', notYet, name="twitter"),       
#Cuentas
    path('accounts/signup/', registro, name="registro"),
    path('accounts/login/', iniciarSesion, name="iniciarSesion"),
    path('accounts/logout/', LogoutView.as_view(template_name="Cuentas/logout.html"), name="cerrarSesion"),
    path('accounts/profile/', editarPerfil, name="editarPerfil"),
    path('accounts/delete/', eliminarPerfil, name="eliminarPerfil"),
    path('accounts/addAvatar/', agregarAvatar, name="agregarAvatar"),
#Blog
    path('blog/', homeBlog, name="blog"),
    path('blog/pages/', ListaPagina.as_view(), name="blogListaPagina"),
    path('blog/pages/<int:pk>', leerPagina, name="blogPagina"),
    path('blog/pages/new/', crearPagina, name="blogCrearPagina"),
    path('blog/pages/edit/<int:pk>', EditarPagina.as_view(), name="blogEditarPagina"),
    path('blog/pages/delete/<int:pk>', EliminarPagina.as_view(), name="blogEliminarPagina"),
    path('blog/pages/addImage/<int:pk>', agregarImagenPagina, name="blogAgregarImagenPagina"),
    path('blog/pages/deleteImage/<int:pk>', EliminarImagenPagina.as_view(), name="blogEliminarImagenPagina"),
#Tienda
    path('notYet/', notYet, name="tienda"),
]

#Imágenes
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
