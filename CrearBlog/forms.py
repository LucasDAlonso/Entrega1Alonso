from django import forms
from pkg_resources import Requirement    

class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(max_length=200)
    fecha_creacion = forms.DateField(Requirement=False)