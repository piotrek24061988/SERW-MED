from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'PiotrG',
        'title': 'News1',
        'content': 'First news content',
        'date_posted': '27.03.2020'
    },
    {
        'author': 'JerzyG',
        'title': 'News2',
        'content': 'Second news content',
        'date_posted': '27.03.2020'
    }
]


class SerwMed:
    def __init__(self):
        pass

    @staticmethod
    def news(request):
        context = {'posts': posts}
        return render(request, 'news.html', context)

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
