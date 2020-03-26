from django.shortcuts import render
from django.http import HttpResponse


def home(requset):
    return HttpResponse('<h1>SERW-MED NEWS</h1>')


def about(request):
    return HttpResponse('<h1>SERW-MED ABOUT</h1>')