from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from bookstore.apps.accounts.forms import CreateUserForms
from bookstore.apps.accounts.models import User
from bookstore.apps.books.models import Favority


class DeleteFavorityBook(LoginRequiredMixin, View):

    success_url = '/accounts/perfil/'

    def get(self, request, pk2):
        get_book = get_object_or_404(Favority, pk=pk2)
        favority = Favority.objects.filter(id=get_book.pk, user=request.user)
        favority.delete()
        return redirect(self.success_url)


class PasswordChangeUser(LoginRequiredMixin, PasswordChangeView):

    template_name = 'accounts/password_reset.html'
    success_url = reverse_lazy('perfil')

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
    success_url = reverse_lazy('list_books')

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
    success_url = reverse_lazy('login_user')


class Login(LoginView):

    template_name = 'accounts/login_user.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list_books')

    def get_success_url(self) -> str:
        return self.success_url


class Logout(LoginRequiredMixin, LogoutView):

    next_page = reverse_lazy('list_books')
