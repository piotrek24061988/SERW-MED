from django.urls import path
from . import views

urlpatterns = [
    path('', views.SerwMed.about, name='serw-med-about'),
    path('news', views.SerwMed.news, name='serw-med-news'),
    path('contact', views.SerwMed.contact, name='serw-med-cont'),
    path('cooperation', views.SerwMed.cooperation, name='serw-med-coop'),
    path('gallery', views.SerwMed.gallery, name='serw-med-gall'),
]