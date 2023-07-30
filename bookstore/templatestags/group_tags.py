from django import template
from django.contrib.auth.models import AbstractUser

register = template.Library()

@register.filter
def is_group(user):
    if not isinstance(user, AbstractUser):
        return False
    return user.groups.exists()

@register.filter
def is_in_group(user, group_name):
    if not isinstance(user, AbstractUser):
        return False
    return user.groups.filter(name=group_name).exists()
