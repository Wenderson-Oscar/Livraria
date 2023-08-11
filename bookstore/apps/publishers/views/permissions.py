from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from bookstore.apps.accounts.models import User
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import redirect


class AskedParticipateEmailGroup(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        name_group = request.GET.get('group_name')
        user_admin_group = User.objects.filter(groups__name=name_group, is_superuser=True, is_active=True).first()

        if user_admin_group:
            get_email_user = self.request.user.email
            get_name_user = self.request.user.name
            subject = f'Participar do Grupo {name_group}'
            message = f'Olá {user_admin_group.username}, Meu nick é {get_name_user}, email: {get_email_user} gostaria de participar do grupo {name_group}!'
            from_email = user_admin_group.email
            recipient_list = [user_admin_group.email]
            send_mail(subject, message, from_email, recipient_list)

            messages.success(self.request, 'Email enviado com sucesso!')
        else:
            messages.error(self.request, 'Ocorreu um erro ao enviar o email.')

        return redirect(reverse('groups:list_groups'))


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

