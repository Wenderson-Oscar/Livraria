from django import forms
from bookstore.apps.books.models import Book
from django.contrib.auth.models import Group


class CreateBookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CreateBookForm, self).__init__(*args, **kwargs)
        self.filter_groups_for_user(user)

    def filter_groups_for_user(self, user):
        if user is not None and user.is_authenticated:
            self.fields['group'].queryset = Group.objects.filter(user=user)

    class Meta:
        model = Book
        fields = ['title', 'cape', 'sinopse', 'year_publication', 'book', 'author', 'gender', 'group']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cape': forms.FileInput(attrs={'class': 'form-control'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-control'}),
            'year_publication': forms.DateInput(attrs={'type': 'date', 'format': 'dd/mm/yyyy','style': 'width: 50%; height: 40px; border-radius: 5px; border: 1px solid #ccc; padding: 0 10px;'}),
            'book': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'gender': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }