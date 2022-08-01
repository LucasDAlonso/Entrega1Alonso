from django.urls import path
from .views import login, register,profile,edit_profile
from django.contrib.auth.views import LogoutView




urlpatterns = [
      path("login/", login , name = "login"),
      path("desloguear/", LogoutView.as_view(template_name="accounts/desloguear.html") , name = "desloguear"),
      path("registrar/", register, name="registrar"),
      path("perfil/", profile , name = "perfil"),
      path("editar_perfil/", edit_profile , name = "editar_perfil"),
      
             
]