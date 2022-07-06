from django.urls import path
from .views import vista1, crear_blog, acerca, listado_blogs

urlpatterns = [
    path('', vista1,name="home"),
    path('crear-blog/',crear_blog,name="crear_blog"),
    path('aboutus/',acerca,name = "aboutus"),
    path("Blogs/",listado_blogs,name ="listado_blogs")

]
