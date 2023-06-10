from chat import views
from django.urls import path

urlpatterns = [
    path('chat/new/', views.CreateComment.as_view(), name='comment_chat'),
]