from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
import datetime
from forum.models import Buku, Forum, Thread, Post

def show_forum(request):
    forums = Forum.objects.all()
    thread = Thread.objects.all()
    
    context = {
    }

    return render(request, "forum.html", context)

def add_post(request):
    if request.method == 'POST':
        body = request.POST.get("body")
        thread = request.POST.get("thread")
        date = str(datetime.datetime.now())
        user = request.user

        new_post = Post(body=body, thread=thread, date=date, user=user)
        new_post.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()