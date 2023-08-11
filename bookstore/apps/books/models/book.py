from django.db import models
from django.contrib.auth.models import Group


class Author(models.Model):

    name = models.CharField(verbose_name='Nome do Autor', max_length=70, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Gender(models.Model):

    gender = models.CharField(verbose_name='Gênero', max_length=20, unique=True)

    def __str__(self):
        return self.gender


class Book(models.Model):

    title = models.CharField(verbose_name='Nome do Livro', max_length=100, unique=True)
    cape = models.ImageField(verbose_name='Capa do Livro', unique=True, upload_to='book/')
    sinopse = models.TextField(verbose_name='Sinopse do Livro')
    year_publication = models.DateField(verbose_name='Ano de Publicação')
    book = models.FileField(verbose_name='Livro', unique=True, upload_to='book/')
    quant_like = models.IntegerField(verbose_name='Curtidas', blank=True, default=0)
    quant_downloads = models.IntegerField(verbose_name='Quantidade de Downloads', blank=True, default=0)
    author = models.ManyToManyField(Author)
    gender = models.ManyToManyField(Gender)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title



