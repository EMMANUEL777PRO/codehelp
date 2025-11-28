from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('tutoriales/', views.tutoriales, name='tutoriales'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
