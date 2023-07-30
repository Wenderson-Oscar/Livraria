from django.urls import path
from bookstore.apps.publishers.views import (CreatePublishersBook, ListPublishersBook, DetailPublishersBook, 
UpdatePublishersBook, DeletePublishersBook, CreateAuthor, CreateGender)


app_name = 'publishers'

urlpatterns = [
    path('create/gender/', CreateGender.as_view(), name='create_gender'),
    path('create/author/', CreateAuthor.as_view(), name='create_author'),
    path('create/', CreatePublishersBook.as_view(), name='create_book'),
    path('list/', ListPublishersBook.as_view(), name='list_book_publishers'),
    path('detail/<int:pk>/', DetailPublishersBook.as_view(), name='detail_book_publishers'),
    path('update/<int:pk>/', UpdatePublishersBook.as_view(), name='update_book_publishers'),
    path('delete/<int:pk>/', DeletePublishersBook.as_view(), name='delete_book_publishers'),
]