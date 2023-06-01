from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateReaderForms


class CreateReader(CreateView):

    template_name = 'readers/create.html'
    form_class = CreateReaderForms
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