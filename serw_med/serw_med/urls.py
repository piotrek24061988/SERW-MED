"""serw_med URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_view
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_view.SerwMedUsers.register, name='serw-med-register'),
    path('login/', users_view.CustomLoginView.as_view(template_name='login.html'), name='serw-med-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='serw-med-logout'),
    path('profile/', users_view.SerwMedUsers.profile, name='serw-med-profile'),
    path('store/', store_views.SerwMedStore.store, name='serw-med-store'),
    path('cart/', store_views.SerwMedStore.cart, name='serw-med-cart'),
    path('checkout/', store_views.SerwMedStore.checkout, name='serw-med-checkout'),
    path('update-item/', store_views.SerwMedStore.updateItem, name='serw-med-update-item'),
    path('process-order/', store_views.SerwMedStore.processOrder, name='serw-med-process-order'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         users_view.CustomSetPasswordView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('', include('news.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
