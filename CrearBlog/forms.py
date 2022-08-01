from django import forms
from ckeditor.fields import RichTextFormField

class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(max_length=200)
    descripcion = RichTextFormField()
    fecha_creacion = forms.DateField(required=False)
    
    
class BusquedaBlogs(forms.Form):
    titulo = forms.CharField(max_length=30)