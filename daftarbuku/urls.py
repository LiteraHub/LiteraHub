from django.urls import path

from daftarbuku.views import add_review_flutter, delete_review_by_id, get_review_json_by_id, search_books, choosebook, post_book_review, search_books_flutter, show_json, show_json_by_id

app_name = "daftarbuku"

urlpatterns = [
    path('', search_books, name='search_books'),
    path('delete_review_by_id/<int:id>/', delete_review_by_id, name='delete_review_by_id'),
    path('add_review_flutter/', add_review_flutter, name='add_review_flutter'),
    path('get_review_json_by_id/<int:id>/', get_review_json_by_id, name='get_review_json_by_id'),
    path('show_json/', show_json, name='show_json'),
    path('show_json_by_id/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('search_books_flutter/', search_books_flutter, name='search_books_flutter'),
    path('post-book-review/<int:id>/', post_book_review, name='post_book_review'),
    path('choose-book/', choosebook, name='choose_book'),
]
