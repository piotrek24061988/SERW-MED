from django.urls import path
#from django.conf.urls import url
from . import views
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView

urlpatterns = [
    path('', views.SerwMed.about, name='serw-med-about'),
    path('news/', views.NewsListView.as_view(), name='serw-med-news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='serw-med-news-detail'),
    path('news/new/', views.NewsCreateView.as_view(), name='serw-med-news-create'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='serw-med-news-update'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='serw-med-news-delete'),
    path('contact/', views.SerwMed.contact, name='serw-med-cont'),
    path('cooperation/', views.SerwMed.cooperation, name='serw-med-coop'),
    path('gallery/', views.SerwMed.gallery, name='serw-med-gall'),
    # Uncommenting this file cause problem with images displaying
    # url(r'.', views.SerwMed.about, name='serw-med-about'),
]