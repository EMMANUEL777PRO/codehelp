from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        # Use the correct field names from AbstractUser: username, password1, password2
        # 'rol' is not a default field on AbstractUser; include only valid fields.
        fields = ['username', 'email', 'password1', 'password2']


