from django import forms
from bookstore.apps.accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForms(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['email']

