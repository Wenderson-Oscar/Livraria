from django.db import models


class Like(models.Model):

    like = models.IntegerField(verbose_name='like', blank=True)
    author = models.IntegerField(verbose_name='id_user', blank=True)

    def __str__(self):
        return f'id_autor: {self.author}'