from django.urls import path
from . import views

urlpatterns = [
    path('', views.SerwMed.about, name='serw-med-about'),
    path('news/', views.NewsListView.as_view(), name='serw-med-news'),
    path('news/<username>', views.UserNewsListView.as_view(), name='serw-med-news-user'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='serw-med-news-detail'),
    path('news/new/', views.NewsCreateView.as_view(), name='serw-med-news-create'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='serw-med-news-update'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='serw-med-news-delete'),
    path('contact/', views.SerwMed.contact, name='serw-med-cont'),
    path('cooperation/', views.SerwMed.cooperation, name='serw-med-coop'),
    path('gallery/', views.SerwMed.gallery, name='serw-med-gall'),
]