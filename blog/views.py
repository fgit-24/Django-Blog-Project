from django.shortcuts import render
from .models import PostModel

# Create your views here.
def index(request):
    posts = PostModel.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')