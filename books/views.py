from django.views.generic import ListView, DetailView
from .models import Book


class ListBooks(ListView):

    model = Book
    template_name = 'books/list_books.html'
    context_object_name = 'books'
    paginate_by = 20


class ListOrderBooks(ListBooks):

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-year_publication')
        return queryset


class DetailBook(DetailView):

    model = Book
    template_name = 'books/detail_book.html'
    context_object_name = 'book'