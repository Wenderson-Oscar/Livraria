from django import forms
from .models import Reader
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForms(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email']


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Reader.objects.create(user=user)
        return user


class ChangerUser(forms.ModelForm):

    perfil = forms.ImageField(required=False)
    data_nascimento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'format': 'dd/mm/yyyy','style': 'width: 20%; height: 40px; border-radius: 5px; border: 1px solid #ccc; padding: 0 10px;'}))
    sexo = forms.ChoiceField(required=False, choices=Reader.CHOICES_SEXO)

    class Meta:
        model = User
        fields = ('name',)

        widget = {
            'name': forms.CharField(required=False)
        }


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            Reader.objects.filter(user=user).update(
                perfil=self.cleaned_data['perfil'],
                data_nascimento=self.cleaned_data['data_nascimento'],
                sexo=self.cleaned_data['sexo']
                )
            user.save()
        return user
    
    