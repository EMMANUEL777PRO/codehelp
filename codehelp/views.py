from django.shortcuts import render

def home(request):
    return render(request, 'codehelp.html')

def comentarios(request):
    return render(request, 'comentarios.html')

def tutoriales(request):
    return render(request, 'tutoriales.html')

def contacto(request):
    return render(request, 'contacto.html')
