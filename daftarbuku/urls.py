from django.urls import path

from daftarbuku.views import search_books, choosebook, post_book_review

urlpatterns = [
    path('', search_books, name='search_book'),
    path('post-book-review/<int:id>/', post_book_review, name='post_book_review'),
    path('choose-book/', choosebook, name='choose_book'),
]
