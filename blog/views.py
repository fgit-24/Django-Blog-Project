from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1 style="color: red">Index Page</h1>')

def about(requst):
    return HttpResponse('<h1 style="color: blue">About Page</h1>')