from django.contrib import admin
from bookstore.apps.chat.models import Chat, ChatPublishers

admin.site.register(Chat)
admin.site.register(ChatPublishers)
