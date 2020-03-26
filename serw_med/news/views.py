from django.shortcuts import render
from django.http import HttpResponse


class NewsViews:
    def __init__(self):
        pass

    @staticmethod
    def homeHTML():
        return b'<h1>SERW-MED NEWS</h1>'

    @staticmethod
    def aboutHTML():
        return b'<h1>SERW-MED ABOUT</h1>'

    @staticmethod
    def home(request):
        print("NewsViews->home(requset:" + str(request) + ")")
        return HttpResponse(NewsViews.homeHTML())

    @staticmethod
    def about(request):
        print("NewsViews->about(requset:" + str(request) + ")")
        return HttpResponse(NewsViews.aboutHTML())