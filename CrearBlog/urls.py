from django.urls import path

from CrearBlog.views import CrearBlog, EditarBlog, EliminarBlog, ListadoBlogs
from .views import vista1, acerca
from . import views

urlpatterns = [
    path('', vista1,name="home"),
    path('aboutus/',acerca,name = "aboutus"),
    path('pages/', views.ListadoBlogs.as_view(), name='listado_blogs'),
    path('create-blog/', views.CrearBlog.as_view(), name='create_blog'),
    path('edit-blog/<int:pk>/', views.EditarBlog.as_view(), name='edit_blog'),
    path('delete-blog/<int:pk>/', views.EliminarBlog.as_view(), name='delete_blog'),
    path('readmore-blog/<int:pk>/', views.MostrarBlog.as_view(), name='readmore_blog'),
    
    

]
