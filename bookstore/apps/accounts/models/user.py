from django.db import models
from django.contrib.auth.models import AbstractUser
from ..models.managers import UserManager


class User(AbstractUser):

    username = None
    name = models.CharField(
        verbose_name='Nome Completo', max_length=70, blank=True, null=True, unique=True,
        error_messages={"unique": ('Nome já Existe!')})
    perfil = models.ImageField(
        verbose_name='Foto de Perfil', blank=True, null=True, upload_to='perfil/', default='not_user.jpg')
    email = models.EmailField(
        verbose_name='E-mail', max_length=200, unique=True,
        error_messages={"unique": ('E-mail já Cadastrado!')})

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'


    def __str__(self) -> str:
        return self.name if self.name else self.email