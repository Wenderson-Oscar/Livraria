from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForms(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['email']


class ChangerUserForms(forms.ModelForm):

 
    class Meta:
        model = User
        fields = ('name', 'perfil')
