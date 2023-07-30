from django import template
from django.contrib.auth.models import AbstractUser

register = template.Library()

@register.filter
def is_in_group(user):
    if not isinstance(user, AbstractUser):
        return False
    return user.groups.exists()
