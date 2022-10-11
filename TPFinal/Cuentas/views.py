from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from Cuentas.forms import *

# Create your views here.

def iniciarSesion(request):
    if request.method == "POST":
        formIS = AuthenticationForm(request, data=request.POST)
        if formIS.is_valid():
            username = formIS.cleaned_data.get('username')
            password = formIS.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return render(request, "Cuentas/loginExitoso.html", {'mensaje': f"Bienvenido {user}."})
    else:
        formIS = AuthenticationForm()
    return render(request, "Cuentas/login.html", {"form":formIS})

def registro(request):
    if request.method == "POST":
        formR = UserCreationFormM(request.POST)
        if formR.is_valid():
            usernameR = formR.cleaned_data.get('username')
            formR.save()
            return render(request, "Cuentas/registroExitoso.html", {'mensaje': f"Se ha creado el usuario {usernameR}."})
    else:
        formR = UserCreationFormM()
    return render(request, "Cuentas/registro.html", {"form":formR})

@login_required
def editarPerfil(request):
    user = request.user
    if request.method =="POST":
        formE = UserEditForm(request.POST)
        if formE.is_valid():
            data = formE.cleaned_data
            user.email = data["email"]
            user.set_password(data['password1'])
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.save()

            return render(request, "Cuentas/editarPerfilExitoso.html", {"mensaje": f"La edición del perfil {user.username} se ha realizado con éxito.", "user":user.username})
    else:
        formE = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})
    return render(request, "Cuentas/editarPerfil.html", {"form":formE, "username":user.username})

@login_required
def eliminarPerfil(request):
    user = request.user
    nombreUser = user.username
    if request.method == "POST":
        user.delete()
        return render(request, "Cuentas/eliminarPerfilExitoso.html", {"mensaje": f"El perfil {nombreUser} ha sido eliminado."})
    else:
        pass
    return render(request, "Cuentas/eliminarPerfil.html", {"username":nombreUser})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        formA = AvatarForm(request.POST, request.FILES)
        if formA.is_valid():
            usuario = User.objects.get(username = request.user)
            avatar = Avatar(user = usuario, imagen = formA.cleaned_data['imagen'])
            avatar.save()
            return render(request, "Cuentas/agregarAvatarExitoso.html", {'mensaje': f"La imagen de {usuario.username} se ha guardado exitosamente"})
    else:
        formA = AvatarForm()
    return render(request, "Cuentas/agregarAvatar.html", {"form":formA})

def notYet(request):
    
    return render(request, "Cuentas/notYet.html")