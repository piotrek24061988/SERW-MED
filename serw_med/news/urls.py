from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.SerwMed.about, name='serw-med-about'),
    path('news', views.SerwMed.news, name='serw-med-news'),
    path('contact', views.SerwMed.contact, name='serw-med-cont'),
    path('cooperation', views.SerwMed.cooperation, name='serw-med-coop'),
    path('gallery', views.SerwMed.gallery, name='serw-med-gall'),
    #url(r'.', views.SerwMed.about, name='serw-med-about'),
]