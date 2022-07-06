from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render

from CrearBlog.forms import FormBlog
from .models import Blog
from datetime  import datetime

# Create your views here.
def vista1 (request):
    return render(request,'index.html')

def crear_blog (request):
    
    if request.method == "POST":
        form = FormBlog(request.POST)
        
        if form.is_valid():
           data = form.cleaned_data
           
           fecha = data.get("fecha_creacion")
           
           blog = Blog(
                    titulo=data.get("titulo"),
                    contenido= data.get("contenido"), 
                    fecha_creacion = fecha if fecha else datetime.now()
            )
           blog.save()
    
    # titulo = request.GET.get("titulo")
    # contenido = request.GET.get("contenido")
    
    # blog = Blog(titulo=titulo,contenido=contenido, fecha_creacion = datetime.now())
    
    form_blog = FormBlog()

    return render (request,"crear_blog.html", {"blog": form_blog} )