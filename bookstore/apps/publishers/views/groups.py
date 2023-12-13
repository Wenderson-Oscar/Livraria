from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


@method_decorator(permission_required('is_staff'), name='dispatch')
class CreateGroup(LoginRequiredMixin, CreateView):

    model = Group
    fields = ('name',)
    template_name = 'publishers/groups/create_group.html'
    success_url = reverse_lazy('groups:list_groups')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Grupo Criado com Sucesso!')
        return response


class ListGroups(LoginRequiredMixin, ListView):
        
    model = Group
    template_name = 'publishers/groups/list_group.html'
    context_object_name = 'groups_list'


class DetailGroup(LoginRequiredMixin, DetailView):
    
    model = Group
    template_name = 'publishers/groups/detail_group.html'
    context_object_name = 'detail_g'


@method_decorator(permission_required('is_staff'), name='dispatch')
class UpdateGroup(LoginRequiredMixin, UpdateView):

    model = Group
    fields = ('name',)
    template_name = 'publishers/groups/update_group.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Grupo Atualizado com Sucesso!')
        return reverse_lazy('groups:detail_group', kwargs={'pk': self.object.pk})


@method_decorator(permission_required('is_staff'), name='dispatch')
class DeleteGroup(LoginRequiredMixin, DeleteView):

    model = Group
    template_name = 'publishers/groups/detail_group.html'
    success_url = reverse_lazy('groups:list_groups')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Grupo com as Permissões Deletado com Sucesso!')
        return response

