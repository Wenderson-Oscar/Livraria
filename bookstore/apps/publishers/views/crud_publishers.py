from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from bookstore.apps.books.models import Book, Author, Gender
from bookstore.apps.publishers.forms import CreateBookForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import Group


class CreatePublishersBook(LoginRequiredMixin, CreateView):
    
    form_class = CreateBookForm
    template_name = 'publishers/create_book.html'
    success_url = '/publishers/list/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Livro Criado com Sucesso!')
        return response


class ListPublishersBook(LoginRequiredMixin, ListView):
    
    model = Book
    template_name = 'publishers/list_book.html'
    context_object_name = 'books_list_publishers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.request.user.groups.first()
        context['group'] = self.model.objects.filter(group=group)
        return context


class DetailPublishersBook(LoginRequiredMixin, DetailView):
    
    model = Book
    template_name = 'publishers/detail_book.html'
    context_object_name = 'detail_b'
    

class UpdatePublishersBook(LoginRequiredMixin, UpdateView):

    model = Book
    fields = ['title', 'cape', 'sinopse', 'year_publication', 'book', 'author', 'gender']
    template_name = 'publishers/update_book.html'

    def get_success_url(self):
        messages.success(self.request, 'Livro Atualizado com Sucesso!')
        return '/publishers/detail/' + str(self.object.pk) + '/'


class DeletePublishersBook(LoginRequiredMixin, DeleteView):

    model = Book
    template_name = 'publishers/detail_book.html'
    success_url = '/publishers/list/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Livro Deletado com Sucesso!')
        return response


class CreateAuthor(LoginRequiredMixin, CreateView):

    model = Author
    fields = '__all__'
    template_name = 'publishers/create_book.html'
    success_url = '/publishers/create/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Autor Criado com Sucesso!')
        return response


class CreateGender(LoginRequiredMixin, CreateView):

    model = Gender
    fields = '__all__'
    template_name = 'publishers/create_book.html'
    success_url = '/publishers/create/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Gênero Criado com Sucesso!')
        return response