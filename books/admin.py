from django.contrib import admin
from .models import Author, Gender, Book, Like, Favority


admin.site.register(Author)
admin.site.register(Gender)
admin.site.register(Book)
admin.site.register(Like)
admin.site.register(Favority)