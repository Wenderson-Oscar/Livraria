from django import forms
from .models import Reader
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateReaderForms(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email']


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            reader = Reader.objects.create(user=user)
        return user
