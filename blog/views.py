from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('index')


def posts_list(request):
    return HttpResponse('posts_list')


def posts_detail(request, id):
    return HttpResponse(f'posts: {id}')
