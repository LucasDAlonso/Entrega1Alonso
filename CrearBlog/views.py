from django.shortcuts import render
from .forms import BusquedaBlogs, FormBlog
from .models import Blog
from datetime  import datetime

def vista1 (request):
    return render(request,'index.html')

def acerca (request):
    return render(request,'about.html')

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
           
           listado_blogs = Blog.objects.all()
           
           return render (request, "listado_blogs.html", {"listado_blogs": listado_blogs})
        
        else:  
            return render (request,"crear_blog.html", {"blog": form} )

    form_blog = FormBlog()

    return render (request,"crear_blog.html", {"blog": form_blog} )

def listado_blogs (request):
    
    nombre_de_busqueda = request.GET.get("titulo")
    if request.GET.get("titulo"):
        listado_blogs = Blog.objects.filter(titulo__icontains = nombre_de_busqueda)
    else:
        
        listado_blogs = Blog.objects.all()
    
    form = BusquedaBlogs()
        
    return render (request, "listado_blogs.html", {"listado_blogs": listado_blogs, "form": form})

