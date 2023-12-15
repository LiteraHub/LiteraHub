import json
from django.shortcuts import render, get_object_or_404
from buku.models import Buku
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from daftarbuku.models import Review
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from .forms import ReviewForm
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
def delete_review_by_id(request, id):
    Review.objects.get(pk=id).delete()
    return JsonResponse({"status": "success"}, status=200)

def get_review_json_by_id(request, id):
    review = Review.objects.filter(Q(book=id))
    return HttpResponse(serializers.serialize("json", review), content_type="application/json")

@csrf_exempt
def add_review_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        buku_id = int(data["book_id"])

        try:
            book = Buku.objects.get(pk=buku_id)
        except Buku.DoesNotExist:
            return JsonResponse({"status": "error"}, status=401)

        user = request.COOKIES.get('user') #Ambil Cookie id
        if (user == None):
            user = request.user

        new_review = Review.objects.create(
            user = request.user,
            review = data["review"],
            created_at=str(datetime.datetime.now()),
            book = book,
            username = user,
        )
        new_review.save()
        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error"}, status=401)

def show_json(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def search_books_flutter(request):
    data = json.loads(request.body)
    try:
        year = int(data["search"])
        hasil_search = Buku.objects.filter(year__icontains=year)
    except:
        hasil_search = Buku.objects.filter(title__icontains=data["search"])
        if not hasil_search.exists():
            hasil_search = Buku.objects.filter(author__icontains=data["search"])
    return HttpResponse(serializers.serialize("json", hasil_search), content_type="application/json")


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
    title = request.GET.get('title', '')
    id = request.GET.get('id', '')
    books = Buku.objects.filter(title__icontains=title)
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
            'username': request.user.username,
        }
        book_list.append(review_json)
    return JsonResponse(book_list, safe=False)


@login_required(login_url='/login')
@csrf_exempt
def post_book_review(request, id):
    book = get_object_or_404(Buku, pk=id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.created_at = str(datetime.datetime.now())
        review.save()
        review_json = {
            'user': {
                'name': request.user.username,
            },
            'id': review.id,
            'review': review.review,
            'created_at': review.created_at,
            'username': request.user.username,
        }
        return JsonResponse(review_json, status=201)
    else:
        errors = form.errors
        print(errors)
    return HttpResponse(status=400)