from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

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
        return render(request, 'profile.html')


