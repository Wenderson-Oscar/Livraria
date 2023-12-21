from bookstore.apps.chat.views import crud_publishers as views_publishers
from django.urls import path

app_name = 'chats_publishers'

urlpatterns = [
    path('create/comment/publishers/<int:pk>/', views_publishers.CreateCommentGroup.as_view(), name='create_comment_publishers'),
    path('edit_messages/<int:pk>/<int:pk1>/', views_publishers.UpdateCommentGroup.as_view(), name='update_comment_publishers'),
    path('delete_messages/publishers/<int:pk>/<int:pk1>/', views_publishers.DeleteCommentGroup.as_view(), name='delete_comment_publishers'),
    path('add_like/comment/publishers/<int:pk1>/<int:pk>/', views_publishers.AddLikeCommentGroup.as_view(), name='add_like_publishers'),
    path('create/comment/response/publishers/<int:pk>/<int:pk1>/', views_publishers.ResponseCommentGroup.as_view(), name='response_comment_publishers'),
]