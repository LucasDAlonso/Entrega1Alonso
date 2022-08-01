from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    titulo = models.CharField(max_length=30) 
    contenido = models.CharField(max_length=200)
    descripcion = RichTextField(null=True)
    fecha_creacion = models.DateField(null=True)

    def __str__(self):
        return f"El titulo del blog es: {self.titulo}"
