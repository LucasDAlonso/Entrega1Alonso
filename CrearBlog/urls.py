from django.urls import path
from .views import vista1, acerca
from . import views

urlpatterns = [
    path('', vista1,name="home"),
    path('aboutus/',acerca,name = "aboutus"),
    path('pages/', views.ListadoBlogs.as_view(), name='listado_blogs'),
    path('crear-blog/', views.CrearBlog.as_view(), name='crear_blog'),
    path('editar-blog/<int:pk>/', views.EditarBlog.as_view(), name='editar_blog'),
    path('eliminar-blog/<int:pk>/', views.EliminarBlog.as_view(), name='eliminar_blog'),
    path('vermas-blog/<int:pk>/', views.MostrarBlog.as_view(), name='vermas_blog'),
    
    

]
