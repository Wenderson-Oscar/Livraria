from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView
from bookstore.apps.chat.models import ChatPublishers
from bookstore.apps.books.models import Like
from django.contrib.auth.mixins import LoginRequiredMixin
from bookstore.apps.chat.views.crud_reader import AddLikeComment


class CreateCommentGroup(LoginRequiredMixin, CreateView):

    model = ChatPublishers
    fields = ['comment']

    def post(self, request, pk):
        if request.POST.get('comment'):
            self.form = self.model(id_group=pk, author=request.user, comment=request.POST.get('comment'))
            self.form.save()
            self.success_url = '/admins/groups/detail/' + str(pk)
            return redirect(self.success_url)
        else:
            return self.form_invalid(self.form)


class UpdateCommentGroup(LoginRequiredMixin, UpdateView):

    model = ChatPublishers
    fields = ['comment']
    template_name = 'publishers/group/detail_group.html'
    success_url = '/admins/groups/detail/'

    def post(self, request, pk, pk1):
        get_id = get_object_or_404(ChatPublishers, pk=pk1)
        if request.POST.get('edit_msg'):
            get_id.comment = request.POST.get('edit_msg')
            get_id.save()
            success_url = '/admins/groups/detail/' + str(pk)
            return redirect(success_url)


class DeleteCommentGroup(AddLikeComment):

    def get(self, request, pk1, pk):
        filt = ChatPublishers.objects.filter(pk=pk1, author=request.user, id_group=pk)
        filt.delete()
        success_url = '/admins/groups/detail/' + str(pk)
        return redirect(success_url)


class AddLikeCommentGroup(LoginRequiredMixin, View):

    def get(self, request, pk1, pk):
        like_comment = get_object_or_404(ChatPublishers, pk=pk1)
        if Like.objects.filter(like=pk1, author=self.request.user.id).count() == 0:
            like = Like(like=pk1, author=self.request.user.id)
            like.save()
            like_comment.quant_like += 1
            like_comment.save()
        elif Like.objects.filter(like=pk1, author=self.request.user.id).count() == 1:
            like = Like.objects.filter(like=pk1, author=self.request.user.id)
            like.delete()
            like_comment.quant_like -= 1
            like_comment.save()
        success_url = '/admins/groups/detail/' + str(pk)
        return redirect(success_url)


class ResponseCommentGroup(LoginRequiredMixin, CreateView):

    model = ChatPublishers
    template_name = 'publishers/group/detail_group.html'
    fields = ['comment']

    def post(self, request, pk, pk1):
        parent_comment = get_object_or_404(ChatPublishers, pk=pk1)
        if request.POST.get('response_msg'):
            self.model.objects.create(
                id_group=pk,
                comment=request.POST.get('response_msg'),
                author=request.user,
                parent_comment=parent_comment
            )
            success_url = '/admins/groups/detail/' + str(pk)
            return redirect(success_url)