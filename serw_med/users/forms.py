from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, SetPasswordForm
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import ClearableFileInput
from .models import Profile


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(label=_('Nazwa użytkownika'))
    password = forms.CharField(label=_('Hasło'), widget=forms.PasswordInput)


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("Nowe hasło"), widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=_("Potwierdź nowe hasło"), widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label=_('Login'))
    email = forms.EmailField(label=_('Email'))
    password1 = forms.CharField(label=_('Hasło'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Powtórz hasło'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label=_('Login'))
    email = forms.EmailField(label=_('Email'))

    class Meta:
        model = User
        fields = ['username', 'email']


class MyClearableFileInput(ClearableFileInput):
    initial_text = 'aktualnie'
    input_text = 'zmień na'


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(label=_("Zdjęcie"), widget=MyClearableFileInput) #required=False,

    class Meta:
        model = Profile
        fields = ['image']
