from django.urls import path
from .views import vista1, crear_blog, acerca, listado_blogs, editar_blog, eliminar_blog, mostrar_blog

urlpatterns = [
    path('', vista1,name="home"),
    path('create-blog/',crear_blog,name="create_blog"),
    path('edit-blog/<int:id>',editar_blog,name="edit_blog"),
    path('delete-blog/<int:id>',eliminar_blog,name="delete_blog"),
    path('readmore-blog/<int:id>',mostrar_blog,name="readmore_blog"),
    path('aboutus/',acerca,name = "aboutus"),
    path('pages/',listado_blogs,name ="listado_blogs")
    

]
