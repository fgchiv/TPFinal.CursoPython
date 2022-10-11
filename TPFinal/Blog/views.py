from datetime import date
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from Blog.forms import *
from Blog.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def homeBlog(request):
    return render(request, "Blog/home.html")

class ListaPagina(ListView):
    model = Pagina

class DetallePagina(DetailView):
    model = Pagina

def leerPagina(request, pk):
    pagina = Pagina.objects.get(id=pk)
    try:
        imagen = ImagenPagina.objects.get(pagina_id=pk)
        contexto= {'pagina':pagina, 'imagen':imagen}
    except:
        contexto= {'pagina':pagina}
    return render(request, "Blog/pagina_detail.html", contexto)

class EliminarPagina(LoginRequiredMixin, DeleteView):
    model = Pagina
    success_url = '/blog/pages/'

class EditarPagina(LoginRequiredMixin, UpdateView):
    model = Pagina
    success_url = '/blog/pages/'
    fields = ['titulo', 'subtitulo', 'cuerpo']

@login_required
def crearPagina(request):
    if request.method == "POST":
        formP = PaginaForm(request.POST)
        if formP.is_valid():
            data = formP.cleaned_data
            pagina = Pagina(
                titulo = data['titulo'], 
                subtitulo = data['subtitulo'], 
                cuerpo = data['cuerpo'],
                fechaPublicacion = date.today(),
                autor = request.user
            )
            pagina.save()
            return redirect('/blog/pages/')
    else:
        formP = PaginaForm()
    return render(request, "Blog/crearPagina.html", {"form":formP})

@login_required
def agregarImagenPagina(request, pk):
    paginaImagen = Pagina.objects.get(id=pk)
    if request.method == "POST":
        formI = ImagenPaginaForm(request.POST, request.FILES)
        if formI.is_valid():
            imagen = ImagenPagina(
                pagina = paginaImagen,
                imagen = formI.cleaned_data['imagen'],
                fechaPublicacion = date.today()
            )
            imagen.save()
            return redirect('/blog/pages/')
    else:
        formI = ImagenPaginaForm()
    return render(request, "Blog/agregarImagenPagina.html", {"form":formI, "titulo":paginaImagen.titulo})

class EliminarImagenPagina(LoginRequiredMixin, DeleteView):
    model = ImagenPagina
    success_url = '/blog/pages/'

def aboutMe(request):
    return render(request, "about.html")

def inicio(request):
    return render(request, "inicio.html")