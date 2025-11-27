from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('tutoriales/', views.tutoriales, name='tutoriales'),
    path('contacto/', views.contacto, name='contacto'),
]
