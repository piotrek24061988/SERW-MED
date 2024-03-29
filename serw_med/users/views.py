from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetConfirmView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CustomAuthenticationForm, CustomSetPasswordForm


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


class CustomSetPasswordView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm


class SerwMedUsers:
    def __init__(self):
        pass

    @staticmethod
    def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Konto dla {username} utworzone')
                return redirect('serw-med-login')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

    @staticmethod
    @login_required
    def profile(request):
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                username = u_form.cleaned_data.get('username')
                messages.success(request, f'Konto dla {username} zaktualizowane')
                return redirect('serw-med-profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, 'profile.html', {'u_form': u_form, 'p_form': p_form})
