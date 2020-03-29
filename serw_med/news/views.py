from django.shortcuts import render
from .models import News


class SerwMed:
    def __init__(self):
        pass

    @staticmethod
    def news(request):
        return render(request, 'news.html', {'newses': News.objects.all()})

    @staticmethod
    def about(request):
        return render(request, 'about.html', {'title': 'my about title'})

    @staticmethod
    def contact(request):
        return render(request, 'contact.html')

    @staticmethod
    def cooperation(request):
        return render(request, 'cooperation.html')

    @staticmethod
    def gallery(request):
        return render(request, 'gallery.html')
