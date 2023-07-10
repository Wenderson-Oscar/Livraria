from bookstore.apps.chat import views
from django.urls import path

urlpatterns = [
    path('edit_messages/<int:pk>/<int:pk1>/', views.UpdateComment.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>/<int:pk1>/', views.DeleteComment.as_view(), name='delete_comment'),
    path('create/comment/response/<int:pk1>/<int:pk>/', views.ResponseComment.as_view(), name='create_comment_response'),
    path('create/comment/new/<int:pk>/', views.CreateComment.as_view(), name='create_comment'),
    path('add_like/comment/<int:pk1>/<int:pk>/', views.AddLikeComment.as_view(), name='add_like'),
    #path('list_comment/<int:pk>/', views.ListComment.as_view(), name='list_chat'),
]