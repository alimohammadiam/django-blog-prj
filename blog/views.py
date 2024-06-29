from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post

# Create your views here.


def index(request):
    return HttpResponse('index')


def posts_list(request):
    post = Post.published.all()
    context = {
        'post': post,
    }
    return render(request, 'tempelete.html', context)


def posts_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except:
        raise Http404('Not Post Found !')
    context = {
        "post": post,
    }
    return render(request, 'template2.html', context)








