from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    
    username= forms.CharField(label='Usuario', max_length=30)
    password1= forms.CharField(label='Password', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir Password',widget=forms.PasswordInput)
    email = forms.EmailField()
    
    

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]
        help_texts = {key: "" for key in fields}

class MyUserEditForm(forms.Form):
    
    first_name= forms.CharField(label='Nombre', max_length=30,required=False)
    last_name= forms.CharField(label='Apellido', max_length=30,required=False)
    email = forms.EmailField(required=False)
    password1= forms.CharField(label='Password', widget=forms.PasswordInput,required=False)
    password2= forms.CharField(label='Repetir Password',widget=forms.PasswordInput,required=False)
    avatar = forms.ImageField(required=False)
    descripcion = forms.CharField(max_length=140)
    link = forms.URLField(max_length= 200,required=False)