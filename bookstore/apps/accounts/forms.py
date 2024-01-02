from django import forms
from bookstore.apps.accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    captcha = CaptchaField()

class CreateUserForms(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()
    
    class Meta:
        model = User
        fields = ['email']

