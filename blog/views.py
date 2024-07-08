from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *

# Create your views here.


def index(request):
    return HttpResponse('index')


def posts_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    context = {
        'posts': posts,
    }
    return render(request, 'blog/list.html', context)


def posts_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    # try:
    #     post = Post.published.get(id=id)
    # except:
    #     raise Http404('Not Post Found !')
    context = {
        "post": post,
    }
    return render(request, 'blog/detail.html', context)


def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = Ticket.objects.create()
            cd = form.cleaned_data
            ticket_obj.message = cd['message']
            ticket_obj.name = cd['name']
            ticket_obj.email = cd['email']
            ticket_obj.phone = cd['phone']
            ticket_obj.subject = cd['subject']
            ticket_obj.save()
            return redirect('blog:ticket')
    else:
        form = TicketForm()
    return render(request, 'forms/ticket.html', {'form': form})






