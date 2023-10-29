from django.urls import path

from daftarbuku.views import search_books, choosebook, post_book_review

app_name = "daftarbuku"

urlpatterns = [
    path('', search_books, name='search_books'),
    path('post-book-review/<int:id>/', post_book_review, name='post_book_review'),
    path('choose-book/', choosebook, name='choose_book'),
]
