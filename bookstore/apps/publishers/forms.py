from django import forms
from bookstore.apps.books.models import Book


class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'cape', 'sinopse', 'year_publication', 'book', 'author', 'gender']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cape': forms.FileInput(attrs={'class': 'form-control'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-control'}),
            'year_publication': forms.DateInput(attrs={'type': 'date', 'format': 'dd/mm/yyyy','style': 'width: 50%; height: 40px; border-radius: 5px; border: 1px solid #ccc; padding: 0 10px;'}),
            'book': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'gender': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }