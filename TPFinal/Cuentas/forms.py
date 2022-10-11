from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Cuentas.models import Avatar

class UserCreationFormM(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario:")
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese la contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "last_name", "first_name"]

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese la contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "last_name", "first_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Seleccione la imagen a cargar. ")
    class Meta:
        model = Avatar
        fields = ['user', 'imagen']