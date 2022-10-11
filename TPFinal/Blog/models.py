from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    fechaPublicacion = models.DateField(blank=True, null=True)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True)

class ImagenPagina(models.Model):
    pagina = models.ForeignKey(Pagina, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to = 'paginasImg', null = True, blank = True)
    fechaPublicacion = models.DateField(blank=True, null=True)