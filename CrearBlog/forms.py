from typing_extensions import Required
from django import forms

class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(max_length=200)
    fecha_creacion = forms.DateField(Required=False)