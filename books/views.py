from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book, Like
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import Chat


class ListBooks(ListView):

    model = Book
    template_name = 'books/list_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return self.model.objects.order_by('-quant_like').all()

    def get_paginate_orphans(self) -> int:
        return 10


class ListOrderPublicationBooks(ListBooks):

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-year_publication').all()
        return queryset


class DetailBook(DetailView):

    model = Book
    template_name = 'books/detail_book.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_comment'] = Chat.objects.filter(id_book=self.kwargs.get('pk')).order_by('-year_publication').all()
        return context


class AddLikeBook(LoginRequiredMixin, View):

    def get(self, request, pk):
        user = request.user.id
        book = get_object_or_404(Book, pk=pk)
        if Like.objects.filter(like=pk, author=user).count() == 0:
            like = Like(like=pk, author=user)
            like.save()
            book.quant_like = book.quant_like + 1
            book.save()
        elif Like.objects.filter(like=pk, author=user).count() == 1:
            like = Like.objects.filter(like=pk, author=user)
            like.delete()
            book.quant_like = book.quant_like - 1
            book.save()
        success_url = '/detail_book/' + str(pk)
        return redirect(success_url)


class CountDownloadsBook(LoginRequiredMixin, DetailBook):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        if self.model.objects.filter(quant_downloads=self.kwargs['pk']).count() >= 0:
            book.quant_downloads = book.quant_downloads + 1
            book.save()
        success_url = '/detail_book/' + str(self.kwargs.get('pk'))
        return redirect(success_url)
    