from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
import datetime
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from forum.models import Thread, Post
from buku.models import Buku

def show_forum(request):
    threads = Thread.objects.filter(forum="recommend")
    posts = Post.objects.all()
    
    context = {
        'threads': threads,
        'posts': posts,
    }

    return render(request, "forum.html", context)

@login_required(login_url='/login')
@csrf_exempt
def add_post(request):
    if request.method == 'POST':
        thread = request.thread
        body = request.POST.get("body")
        date = str(datetime.datetime.now())
        user = request.user

        new_post = Post(body=body, thread=thread, date=date, user=user)
        new_post.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='/login')
@csrf_exempt
def add_thread(request):
    if request.method == 'POST':
        author = request.user
        forum = request.POST.get("forum")
        name = request.POST.get("name")
        date = str(datetime.datetime.now())
        buku_title = request.POST.get("buku")
        
        try:
            buku = Buku.objects.get(title=buku_title)
        except Buku.DoesNotExist:
            buku = None

        new_thread = Thread(author=author, name=name, forum=forum, date=date, buku=buku)
        new_thread.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()


@login_required(login_url='/login')
def writer(request):
    threads = Thread.objects.filter(forum="penulis")
    posts = Post.objects.all()
    
    context = {
        'threads': threads,
        'posts': posts,
    }

    return render(request, "forum_writers.html", context)

@login_required(login_url='/login')
def trending(request):
    threads = Thread.objects.annotate(post_count=Count('post')).order_by('-post_count')
    posts = Post.objects.all()
    
    context = {
        'threads': threads,
        'posts': posts,
    }
    return render(request, "forum_trending.html", context)

@login_required(login_url='/login')
def explore(request):
    threads = Thread.objects.all()
    posts = Post.objects.all()
    
    context = {
        'threads': threads,
        'posts': posts,
    }
    return render(request, "forum_explore.html", context)

def to_thread(request):
    threads = Thread.objects.all()
    posts = Post.objects.all()
    
    context = {
        'threads': threads,
        'posts': posts,
    }
    return render(request, "threads.html", context)

def get_threads(request):
    threads = Thread.objects.all()
    return HttpResponse(serializers.serialize('json', threads))

def get_post(request):
    posts = Post.objects.all()
    return HttpResponse(serializers.serialize('json', posts))

def get_books_json(request):
    books = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

def get_time(request):
    return str(datetime.datetime.now())