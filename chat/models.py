from django.db import models
from accounts.models import User


class Chat(models.Model):
    
    id_book = models.IntegerField(verbose_name='id_book', blank=True, null=True)
    comment = models.CharField(verbose_name='Comentário', max_length=250, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    year_publication = models.DateTimeField('Ano de Publicação', auto_now_add=True)
    quant_like = models.IntegerField('Curtidas', blank=True, default=0)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')

    def __str__(self):
        return str(self.author)
