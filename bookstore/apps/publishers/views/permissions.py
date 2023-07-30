from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from bookstore.apps.accounts.models import User
from django.shortcuts import get_object_or_404


@method_decorator(permission_required('is_staff'), name='dispatch')
class RemoveAdminGroup(LoginRequiredMixin, UpdateView):

    model = Group
    fields = []
    template_name = 'publishers/group/detail_group.html'

    def get_success_url(self):
        return reverse_lazy('groups:detail_group', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        group = self.get_object()
        user_pk = self.request.POST.get('user')
        user = get_object_or_404(User, pk=user_pk)
        user.is_superuser = False
        user.save()
        messages.success(self.request, 'Administrator Removido do Grupo com Sucesso!')
        return response


@method_decorator(permission_required('is_staff'), name='dispatch')
class AddAdminGroup(LoginRequiredMixin, UpdateView):

    model = Group
    fields = []
    template_name = 'publishers/group/add_user_group.html'

    def get_success_url(self):
        return reverse_lazy('groups:detail_group', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        group = self.get_object()
        user_pk = self.request.POST.get('user')
        user = get_object_or_404(User, pk=user_pk)
        user.is_superuser = True
        user.save()
        group.user_set.add(user)
        messages.success(self.request, 'Administrador Adicionado ao Grupo com Sucesso!')
        return response


@method_decorator(permission_required('superuser'), name='dispatch')
class AddUserGroup(LoginRequiredMixin, UpdateView):

    model = Group
    fields = []
    template_name = 'publishers/permissions/add_user_group.html'

    def get_success_url(self):
        return reverse_lazy('groups:detail_group', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        group = self.get_object()
        user_pk = self.request.POST.get('user')
        user = get_object_or_404(User, pk=user_pk)
        group.user_set.add(user)
        messages.success(self.request, 'Usuário Adicionado ao Grupo com Sucesso!')
        return response


@method_decorator(permission_required('superuser'), name='dispatch')
class RemoveUserGroup(LoginRequiredMixin, UpdateView):

    model = Group
    fields = []
    template_name = 'publishers/groups/detail_group.html'

    def get_success_url(self):
        return reverse_lazy('groups:detail_group', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        group = self.get_object()
        user_pk = self.request.POST.get('user')
        user = get_object_or_404(User, pk=user_pk)
        group.user_set.remove(user)
        messages.success(self.request, 'Usuário Removido do Grupo com Sucesso!')
        return response
        

@method_decorator(permission_required('superuser'), name='dispatch')
class UpdateNameGroup(LoginRequiredMixin, UpdateView):

    model = Group
    fields = ['name']
    template_name = 'publishers/groups/detail_group.html'

    def get_success_url(self):
        messages.success(self.request, 'Nome do Grupo Atualizado com Sucesso!')
        return reverse_lazy('groups:detail_group', kwargs={'pk': self.object.pk})

