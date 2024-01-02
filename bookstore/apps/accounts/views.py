from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from bookstore.apps.accounts.forms import CreateUserForms, LoginForm
from bookstore.apps.accounts.models import User
from bookstore.apps.books.models import Favority
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


class RecoverPassword(SuccessMessageMixin, PasswordResetView):
    
    template_name = 'accounts/recover_password.html'
    email_template_name = 'accounts/recover_password_email.html'
    subject_template_name = 'accounts/recover_password_object'
    success_message = 'Enviamos um e-mail com instruções para redefinir sua senha.'
    success_url = reverse_lazy('accounts:login_user')


class PasswordChangeUser(LoginRequiredMixin, PasswordChangeView):

    template_name = 'accounts/password_reset_update.html'
    success_url = reverse_lazy('accounts:perfil')

    def get_object(self):
        return self.request.user.id


class UpdateUser(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/create.html'
    fields = ['name','perfil']
    success_url = '/accounts/perfil/'

    def get_object(self):
        return self.request.user


class DeleteUser(LoginRequiredMixin, DeleteView):

    model = User
    template_name = 'accounts/delete_user.html'
    success_url = reverse_lazy('books:list_books')

    def set_valid_delete(self):
        self.request.user.delete()

    def get_object(self):
        return self.request.user
    
    def get_success_url(self) -> str:
        return self.success_url


class PerfilDetail(LoginRequiredMixin, DetailView):

    model = User
    template_name = 'accounts/perfil.html'
    context_object_name = 'perfil'

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_favoritys'] = Favority.objects.filter(user=self.request.user).all()
        return context


class CreateUser(CreateView):

    template_name = 'accounts/create.html'
    form_class = CreateUserForms
    success_url = reverse_lazy('accounts:login_user')


class Login(LoginView):

    template_name = 'accounts/login_user.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('books:list_books')

    def get_success_url(self) -> str:
        return self.success_url


class Logout(LoginRequiredMixin, LogoutView):

    next_page = reverse_lazy('books:list_books')
