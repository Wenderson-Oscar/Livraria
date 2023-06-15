from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView
from .models import Chat
from books.models import Like
from django.contrib.auth.mixins import LoginRequiredMixin


class ResponseComment(LoginRequiredMixin, CreateView):

    model = Chat
    fields = ['comment']

    def post(self, request, pk, pk1):
        get_comment = get_object_or_404(Chat, pk=pk1)
        filter = self.model.objects.filter(id_book=pk, author=get_comment.author, comment=get_comment.comment)
        if filter:
            if request.POST.get('response_msg'):
                response = filter.update(id_response=request.user.pk, response=request.POST.get('response_msg'))
                success_url = '/detail_book/' + str(pk)
                return redirect(success_url)
            else:
                return self.form_invalid(self.response)


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
        if Like.objects.filter(like=pk1, author=request.user.id).count() == 0:
            like = Like(like=pk1, author=request.user.id)
            like.save()
            like_comment.quant_like += 1
            like_comment.save()
        elif Like.objects.filter(like=pk1, author=request.user.id).count() == 1:
            like = Like.objects.filter(like=pk1, author=request.user.id)
            like.delete()
            like_comment.quant_like -= 1
            like_comment.save()
        success_url = '/detail_book/' + str(pk)
        return redirect(success_url)
