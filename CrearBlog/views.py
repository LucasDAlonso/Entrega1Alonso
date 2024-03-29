from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BusquedaBlogs
from .models import Blog


def vista1 (request):
    return render(request,'index.html')

def acerca (request):
    return render(request,'about.html')


class ListadoBlogs(ListView):
    model=Blog
    template_name = 'Blog/listado_blogs.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaBlogs()
        return context
    
    
class CrearBlog(LoginRequiredMixin,CreateView):
    model=Blog
    template_name = 'Blog/crear_blog.html'
    success_url = '/pages'
    fields = ['titulo', "subtitulo", "contenido","autor",'fecha_creacion',"imagen"]



class EditarBlog(LoginRequiredMixin,UpdateView):
    model=Blog
    template_name = 'Blog/editar_blog.html'
    success_url = '/pages'
    fields = ['titulo', "subtitulo","contenido","autor","fecha_creacion","imagen"]


class EliminarBlog(LoginRequiredMixin, DeleteView):
    model=Blog
    template_name = 'Blog/eliminar_blog.html'
    success_url = '/pages/'


class MostrarBlog(DetailView):
    model = Blog
    template_name = 'Blog/ver_mas.html'

def listado_blogs (request):
    
    nombre_de_busqueda = request.POST.get("Titulo")
    if request.POST.get("Titulo"):
        listado_blogs = Blog.objects.filter(titulo__icontains = nombre_de_busqueda)
    else:
        listado_blogs = Blog.objects.all()
    
    form = BusquedaBlogs()
        
    return render (request, "Blog/listado_blogs.html", {"listado_blogs": listado_blogs, "form": form})

