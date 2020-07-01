from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_view

urlpatterns = [
    path('register/', users_view.SerwMedUsers.register, name='serw-med-register'),
    path('login/', users_view.CustomLoginView.as_view(template_name='login.html'), name='serw-med-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='serw-med-logout'),
    path('profile/', users_view.SerwMedUsers.profile, name='serw-med-profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         users_view.CustomSetPasswordView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]