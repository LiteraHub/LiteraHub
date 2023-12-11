from django.shortcuts import render, get_object_or_404
from buku.models import Buku
from django.views.decorators.csrf import csrf_exempt
from daftarbuku.models import Review
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from .forms import ReviewForm
import datetime

# Create your views here.
def search_books(request):
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')
    year = request.GET.get('yearbook', '')

    data = Buku.objects.all()

    if 'title' in request.GET:
        data = data.filter(title__icontains=title)
    if 'author' in request.GET:
        data = data.filter(author__icontains=author)
    if 'yearbook' in request.GET:
        data = data.filter(year__icontains=year)
    context = {
        'data': data,
        'review_form': ReviewForm(),
    }
    return render(request, 'daftarbuku.html', context)


def choosebook(request):
    print("halo2")
    title = request.GET.get('title', '')
    id = request.GET.get('id', '')
    print(id)
    books = Buku.objects.filter(title__icontains=title)
    print(books)
    book = get_object_or_404(Buku, pk=id)
    review_list = Review.objects.filter(book=book)
    book_list = []
    for buku in books:
        book_json = {
            'isbn': buku.isbn,
            'title': buku.title,
            'author': buku.author,
            'year': buku.year,
            'img': buku.img,
        }
        book_list.append(book_json)
    for review in review_list:
        review_json = {
            'user': {
                'name': request.user.username,
            },
            'id': review.id,
            'review': review.review,
            'created_at': review.created_at,
        }
        book_list.append(review_json)
    return JsonResponse(book_list, safe=False)


<<<<<<< HEAD
@login_required(login_url='/login')
=======
>>>>>>> 6dcd09b358ebc9dcac7c707686172bb9d0686c4c
@csrf_exempt
def post_book_review(request, id):
    print(id)
    print("ini postbook")
    book = get_object_or_404(Buku, pk=id)
    print(book)
    form = ReviewForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        print("test")
        review = form.save(commit=False)
        review.book = book
        print(review.book)
        # review.user = request.user
        review.created_at = str(datetime.datetime.now())
        review.save()
        review_json = {
            'user': {
                'name': request.user.username,
            },
            'id': review.id,
            'review': review.review,
            'created_at': review.created_at,
        }
        return JsonResponse(review_json, status=201)
    else:
        errors = form.errors
        print(errors)
    return HttpResponse(status=400)