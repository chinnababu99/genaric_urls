from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def string1 (request):
    return HttpResponse('<h1>Hello world</h1>')

def string2(request):
    return HttpResponse('<h1>hello good morning</h1>')
