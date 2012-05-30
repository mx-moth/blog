from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    posts = Post.objects.published()
    
    return render(request, 'blog/index.html', {
        'posts': posts,
    })

def view(request, slug):
    post = get_object_or_404(Post.objects.published(), slug=slug, published=True)

    return render(request, 'blog/view.html', {
        'post': post
    })

def archive(request, year=None, month=None, day=None):
    pass
