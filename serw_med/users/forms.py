from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label=_('Login'))
    email = forms.EmailField(label=_('Email'))
    password1 = forms.CharField(label=_('Hasło'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Powtórz hasło'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
