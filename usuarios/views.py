from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth.forms import AuthenticationForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada correctamente. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f"Bienvenido {usuario.username}")
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente")
    return redirect('home')
