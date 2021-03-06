# carga el modulo de forms de django
from django import forms

# carga el formulario de creacion de usuarios de django
from django.contrib.auth.forms import UserCreationForm

# carga el modelo de User de django
from django.contrib.auth.models import User

# Creamos nuestro formulario que hereda el de django
class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='Nombre de usuario')
    email=forms.CharField(label='Correo',widget=forms.EmailInput)
    telefono = forms.CharField(
        label='Telefono',
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control form-control-sm"}),
    )
    direccion = forms.CharField(
        label='direccion',
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control form-control-sm"}),
    )
    # telefono=forms.CharField(label='Telefono',widget=forms.CharField) 
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirme contraseña',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields}