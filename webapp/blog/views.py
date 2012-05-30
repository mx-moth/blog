from django.shortcuts import render
from blog.models import Post

def index(request):
    posts = Post.objects.published()
    
    return render(request, 'blog/index.html', {
        'posts': posts,
    })

def view(request, slug):
    pass

def archive(request, year=None, month=None, day=None):
    pass
