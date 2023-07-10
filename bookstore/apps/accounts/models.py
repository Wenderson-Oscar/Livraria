from django.db import models
from django.contrib.auth.models import (AbstractUser, UserManager)


class UserManager(UserManager):

    def create_user(self, email: str, password=None, **extra_fields):

        if not email:
            raise ValueError("O E-mail é Obrigatório")

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email: str, password=None, **extra_fields):
     
        if not email:
            raise ValueError("O E-mail è Obrigatório")

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user


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