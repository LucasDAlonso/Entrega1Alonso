from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    titulo = models.CharField(max_length=30) 
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField(null=True)
    autor = models.CharField(max_length=30, blank=True) 
    fecha_creacion = models.DateField(null=True)
    imagen = models.ImageField(upload_to= "blos", null=True, blank=True)
    
    def __str__(self):
        return f"El titulo del blog es: {self.titulo}"
