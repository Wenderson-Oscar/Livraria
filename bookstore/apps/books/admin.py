from django.contrib import admin
from bookstore.apps.books.models import Author, Gender, Book, Like, Favority


admin.site.register(Author)
admin.site.register(Gender)
admin.site.register(Book)
admin.site.register(Like)
admin.site.register(Favority)