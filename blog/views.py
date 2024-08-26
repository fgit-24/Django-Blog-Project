from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import PostModel
from .forms import PostModelForm

# Create your views here.
def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(PostModel, id=pk)
    
    context = {
        'post': post,
    }
    
    return render(request, 'blog/post_detail.html', context)

def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    context = {

    }
    return render(request, 'blog/post_edit.html', context)