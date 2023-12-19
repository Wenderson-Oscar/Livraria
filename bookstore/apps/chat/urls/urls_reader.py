from bookstore.apps.chat.views import crud_reader as views_reader
from django.urls import path

app_name = 'chats'

urlpatterns = [
    path('edit_messages/<int:pk>/<int:pk1>/', views_reader.UpdateComment.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>/<int:pk1>/', views_reader.DeleteComment.as_view(), name='delete_comment'),
    path('create/comment/response/<int:pk1>/<int:pk>/', views_reader.ResponseComment.as_view(), name='create_comment_response'),
    path('create/comment/new/<int:pk>/', views_reader.CreateComment.as_view(), name='create_comment'),
    path('add_like/comment/<int:pk1>/<int:pk>/', views_reader.AddLikeComment.as_view(), name='add_like'),
]