from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsViews.home, name='news-home'),
    path('about/', views.NewsViews.about, name='news-about'),
]