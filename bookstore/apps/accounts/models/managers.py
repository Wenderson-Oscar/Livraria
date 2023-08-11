from django.contrib.auth.models import UserManager


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

