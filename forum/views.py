import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
import datetime
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from forum.models import Thread, Post
from buku.models import Buku
from django.contrib.auth.models import User

# def show_threads to show all the threads. Main page of forum
def show_forum(request):
    threads = Thread.objects.all().order_by('-date')
    books = Buku.objects.all().order_by('title')
    
    context = {
        'threads': threads,
        'books': books,
    }
    return render(request, 'forum.html', context)
    

#def show_posts to show all the posts of a thread
def show_posts(request, id):
    posts = Post.objects.filter(pk=id).order_by('date')
    
    context = {
        'posts': posts
    }
    return render(request, 'threads.html', context)

# To add a new thread in the website
@login_required(login_url='/login')
def add_thread(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get("name")
        buku = request.POST.get("buku")
        date = str(datetime.datetime.now())
        
        new_thread = Thread.objects.create(
                user=user,
                name=name,
                buku=buku,
                date=date
            )
        
        result = {
            'pk':new_thread.pk,
            'user':new_thread.user.username,
            'name':new_thread.name,
            'buku':new_thread.buku,
            'date':new_thread.date.date()
        }
        return JsonResponse(result, status=200)
    return render(request, "forum.html")

# add posts to a thread in the website
@login_required(login_url='/login')
def add_post(request, id):
    thread = Thread.objects.get(pk=id)
    if request.method == "POST":
        user = request.user
        body = request.POST.get("body")
        date = str(datetime.datetime.now())
        
        new_post = Post.objects.create(
                user=user,
                body=body,
                thread = thread,
                date=date
            )
        
        result = {
            'pk':new_post.pk,
            'user':new_post.user.username,
            'body':new_post.body,
            'date':new_post.date.date()
        }
        return JsonResponse(result, status=200)
    return render(request, "threads.html")

#add threads in the flutter app
@login_required(login_url='/login')
@csrf_exempt
def add_thread_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get('buku')
        buku = None
        if (title != 'null'):
            try:
                buku = Buku.objects.get(title=title)
            except:
                buku = None #buku tidak ada
        else:
            buku = None #tidak pilih buku
            
        new_thread = Thread.objects.create(
            user=request.user,
            name=data["name"],
            buku=buku,
            date=data["date"]
        )
        
        new_thread.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='/login')
@csrf_exempt
def add_post_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            thread_id = data.get('thread')
            thread = Thread.objects.get(pk=thread_id)

            new_post = Post.objects.create(
                user=request.user,
                body=data["body"],
                thread=thread,
                date=data["date"]
            )

            new_post.save()

            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "error": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid method"}, status=401)

    
#To get the json of the threads
def get_json_threads(request):
    data = Thread.objects.all().order_by('-date')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
#To get the json of the posts
def get_json_posts(request, id):
    data = Post.objects.filter(thread=id).order_by('-date')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
#To get the json of the books
def get_json_buku(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#get buku by title
def get_buku_by_title(request, title):
    data = Buku.objects.filter(title=title)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#get buku by pk
def get_buku_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#chek posts
def get_all_posts(request):
    data = Post.objects.all().order_by('-date')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#mapping usernames to ids
def get_usernames(request):
    users = User.objects.all()
    user_mapping = {user.id: user.username for user in users}

    return JsonResponse({'user_mapping': user_mapping})
