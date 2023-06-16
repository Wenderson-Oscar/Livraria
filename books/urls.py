from books import views
from django.urls import path


urlpatterns = [
    path('', views.ListBooks.as_view(), name='list_books'),
    path('detail_book/<int:pk>/', views.DetailBook.as_view(), name='detail_book'),
    path('list_books/published/', views.ListOrderPublicationBooks.as_view(), name='list_books_order'),
    path('add_like/book/<int:pk>/', views.AddLikeBook.as_view(), name='like_book'),
    path('count_downlodas/book/<int:pk>/', views.CountDownloadsBook.as_view(), name='count_downl'),
]