from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from bookstore.apps.chat.models import Chat
from bookstore.apps.books.models import Like
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdateComment(LoginRequiredMixin, UpdateView):

    model = Chat
    fields = ['comment']
    template_name = 'books/detail_book.html'
    success_url = '/detail_book/'

    def post(self, request, pk, pk1):
        get_id = get_object_or_404(Chat, pk=pk1)
        if request.POST.get('edit_msg'):
            get_id.comment = request.POST.get('edit_msg')
            get_id.save()
            success_url = '/detail_book/' + str(pk)
            return redirect(success_url)


class ResponseComment(LoginRequiredMixin, CreateView):

    model = Chat
    template_name = 'books/detail_book.html'
    fields = ['comment']

    def post(self, request, pk, pk1):
        parent_comment = get_object_or_404(Chat, pk=pk1)
        if request.POST.get('response_msg'):
            self.model.objects.create(
                id_book=pk,
                comment=request.POST.get('response_msg'),
                author=request.user,
                parent_comment=parent_comment
            )
            success_url = '/detail_book/' + str(pk)
            return redirect(success_url)
    

class CreateComment(LoginRequiredMixin, CreateView):

    model = Chat
    fields = ['comment']

    def post(self, request, pk):
        if request.POST.get('comment'):
            self.form = self.model(id_book=pk, author=request.user, comment=request.POST.get('comment'))
            self.form.save()
            self.success_url = '/detail_book/' + str(pk)
            return redirect(self.success_url)
        else:
            return self.form_invalid(self.form)


class AddLikeComment(LoginRequiredMixin, View):

    def get(self, request, pk1, pk):
        like_comment = get_object_or_404(Chat, pk=pk1)
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
        success_url = '/detail_book/' + str(pk)
        return redirect(success_url)


class DeleteComment(AddLikeComment):

    def get(self, request, pk1, pk):
        filt = Chat.objects.filter(pk=pk1, author=request.user, id_book=pk)
        filt.delete()
        success_url = '/detail_book/' + str(pk)
        return redirect(success_url)