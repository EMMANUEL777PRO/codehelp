from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada correctamente. ¡Ahora puedes iniciar sesión!')
            return redirect('register') 
    else:
        form = UserCreationForm()

    
    return render(request, 'usuarios/register.html', {'form': form})
