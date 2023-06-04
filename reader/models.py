from django.db import models
from accounts.models import User


class Reader(models.Model):

    CHOICES_SEXO = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OUTROS')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil = models.ImageField(verbose_name='Foto de Perfil', blank=True, null=True, upload_to='perfil/')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True ,choices=CHOICES_SEXO)
    data_entrada = models.DateTimeField(verbose_name='Date de Criação da Conta', auto_now_add=True)


    def __str__(self):
        return self.user.name if self.user.name else self.user.email
