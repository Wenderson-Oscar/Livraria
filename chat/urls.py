from chat import views
from django.urls import path

urlpatterns = [
    path('create/comment/response/<int:pk1>/<int:pk>/', views.ResponseComment.as_view(), name='create_comment_response'),
    path('create/comment/new/<int:pk>/', views.CreateComment.as_view(), name='create_comment'),
    path('add_like/comment/<int:pk1>/<int:pk>/', views.AddLikeComment.as_view(), name='add_like'),
]