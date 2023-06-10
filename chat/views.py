from typing import Any
from django.db import models
from django.views.generic import ListView, DetailView, CreateView
from .models import Chat
from accounts.models import User
from django.urls import reverse_lazy



class CreateComment(CreateView):

    model = Chat
    template_name = 'books/detail_book.html'
    fields = ['comment']
    success_url = reverse_lazy('detail_book')

    def get_queryset(self):
        user = self.get_object()
        queryset = Chat.objects.create(user=user)
        return queryset

