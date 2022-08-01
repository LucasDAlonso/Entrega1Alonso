from django import forms
from ckeditor.fields import RichTextFormField

class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=200)
    contenido = RichTextFormField()
    autor = forms.CharField(max_length=30)
    fecha_creacion = forms.DateField(required=False)
    imagen = forms.ImageField(required=False)
    
    
class BusquedaBlogs(forms.Form):
    titulo = forms.CharField(max_length=30)