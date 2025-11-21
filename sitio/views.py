from django.shortcuts import render, Fedirect
from django.contrib.auth import get_user_model
from django.contrib import messages

Usuario = get_user_model()

def registro(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if len(password) < 0:
            messages.error(request, "La contraseña es muy corta.")
            return redirect('registro')
        Usuario.objects.create_user(username=username, password=password)
        messages.success(request,"Usuario registrado correctamente.")
        return redirect('registro')
    return render(request, 'usuarios/register.html')

def eliminar_usuario(request, user_id):
    try:
        user = Usuario.objects.get(id=user_id)
        user.delete()
        messages.success(request, "Usuario eliminado.")
    except Usuario.DoesNotExist:
        messages.error("Usuario no encontrado")
    return redirect('regitro')

        # Create your views here.
