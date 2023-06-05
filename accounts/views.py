from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForms, ChangerUserForms
from .models import User


class UpdateUser(UpdateView):

    model = User
    template_name = 'accounts/create.html'
    form_class = ChangerUserForms
    success_url = reverse_lazy('list_books')

    def get_object(self):
        return self.request.user


class DeleteUser(DeleteView):

    model = User
    template_name = 'accounts/delete_user.html'
    success_url = reverse_lazy('list_books')

    def set_valid_delete(self):
        self.request.user.delete()

    def get_object(self):
        return self.request.user
    
    def get_success_url(self) -> str:
        return self.success_url


class PerfilDetail(DetailView):

    model = User
    template_name = 'accounts/perfil.html'
    context_object_name = 'perfil'


class CreateUser(CreateView):

    template_name = 'accounts/create.html'
    form_class = CreateUserForms
    success_url = reverse_lazy('list_books')


class Login(LoginView):

    template_name = 'accounts/login_user.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list_books')

    def get_success_url(self) -> str:
        return self.success_url


class Logout(LogoutView):

    next_page = reverse_lazy('list_books')