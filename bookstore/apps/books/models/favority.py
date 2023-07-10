from django.db import models
from bookstore.apps.books.models import Book
from bookstore.apps.accounts.models import User


class Favority(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
