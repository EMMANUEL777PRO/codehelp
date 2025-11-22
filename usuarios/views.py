
from django.shortcuts import render

def register(request):
    return render(request, 'usuarios/register.html')

