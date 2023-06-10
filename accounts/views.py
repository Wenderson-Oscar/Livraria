from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateUserForms
from .models import User


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

    def post(self, request, *args, **kwargs):
        contex = super().post(request, *args, **kwargs)
        contex = request.session.flush()
        return contex