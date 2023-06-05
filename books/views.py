from typing import Any
from django.db import models
from django.views.generic import ListView, DetailView
from .models import Book


class ListBooks(ListView):
    
    model = Book
    template_name = 'books/list_books.html'
    context_object_name = 'books'


class DetailBook(DetailView):

    model = Book
    template_name = 'books/detail_book.html'
    context_object_name = 'book'