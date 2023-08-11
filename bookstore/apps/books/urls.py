from bookstore.apps.books import views
from django.urls import path

app_name = 'books'

urlpatterns = [
    path('', views.ListBooks.as_view(), name='list_books'),
    path('search/', views.SearchBook.as_view(), name='book_search'),
    path('delete/favority/<int:pk2>/', views.DeleteFavorityBook.as_view(), name='delete_favority'),
    path('add_book/favority/<int:pk>/', views.AddFavorityBook.as_view(), name='add_favority'),
    path('detail_book/<int:pk>/', views.DetailBook.as_view(), name='detail_book'),
    path('list_books/published/', views.ListOrderPublicationBooks.as_view(), name='list_books_order'),
    path('add_like/book/<int:pk>/', views.AddLikeBook.as_view(), name='like_book'),
    path('count_downlodas/book/<int:pk>/', views.CountDownloadsBook.as_view(), name='count_downl'),
]