from django.db import models
from accounts.models import User


class Chat(models.Model):

    comment = models.CharField(verbose_name='Comentário', max_length=250, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.author
