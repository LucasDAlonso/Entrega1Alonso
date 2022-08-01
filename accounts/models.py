from django.db import models
from django.contrib.auth.models import User

class MoreUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)
    descripcion = models.CharField(max_length=140, null=True)
    link = models.URLField(max_length= 200,null=True, blank=True)    
