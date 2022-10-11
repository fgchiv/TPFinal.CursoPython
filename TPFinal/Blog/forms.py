from django import forms
from ckeditor.widgets import CKEditorWidget
from Blog.models import *

class PaginaForm(forms.Form):
    titulo=forms.CharField()
    subtitulo=forms.CharField()
    cuerpo=forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Pagina

class ImagenPaginaForm(forms.Form):
    imagen = forms.ImageField(label="Seleccione la imagen a cargar:")
    class Meta:
        model = ImagenPagina
        fields = ['pagina', 'imagen', 'fechaPublicacion']
