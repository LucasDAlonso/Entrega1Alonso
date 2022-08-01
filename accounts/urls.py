from django.urls import path
from .views import login, register,profile,edit_profile
from django.contrib.auth.views import LogoutView




urlpatterns = [
      path("login/", login , name = "login"),
      path("logout/", LogoutView.as_view(template_name="accounts/logout.html") , name = "logout"),
      path("register/", register, name="register"),
      path("profile/", profile , name = "profile"),
      path("edit_profile/", edit_profile , name = "edit_profile"),
      
             
]