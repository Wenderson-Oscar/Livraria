from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForms, ChangerUser
from .models import Reader
from accounts.models import User


class UpdateUser(UpdateView):

    model = User
    template_name = 'readers/create.html'
    form_class = ChangerUser
    success_url = reverse_lazy('list_books')

    def get_object(self):
        return self.request.user


class DeleteUser(DeleteView):

    model = User
    template_name = 'readers/delete_user.html'
    success_url = reverse_lazy('list_books')

    def get_object(self):
        return self.request.user.email
    
    def get_success_url(self) -> str:
        return self.success_url


class PerfilDetail(DetailView):

    model = Reader
    template_name = 'readers/perfil.html'
    context_object_name = 'perfil'


class CreateUser(CreateView):

    template_name = 'readers/create.html'
    form_class = CreateUserForms
    success_url = reverse_lazy('list_books')


class Login(LoginView):

    template_name = 'login_user.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list_books')

    def get_success_url(self) -> str:
        return self.success_url


class Logout(LogoutView):

    next_page = reverse_lazy('list_books')