from books import views
from django.urls import path


urlpatterns = [
    path('', views.ListBooks.as_view(), name='list_books'),
    path('detail_book/<int:pk>/', views.DetailBook.as_view(), name='detail_book'),
]