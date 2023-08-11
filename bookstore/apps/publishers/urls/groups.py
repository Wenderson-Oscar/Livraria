from django.urls import path
from bookstore.apps.publishers.views import (CreateGroup, ListGroups, DetailGroup, UpdateGroup, DeleteGroup)

app_name = 'groups'

urlpatterns = [
    path('create/', CreateGroup.as_view(), name='create_group'),
    path('list/', ListGroups.as_view(), name='list_groups'),
    path('detail/<int:pk>/', DetailGroup.as_view(), name='detail_group'),
    path('update/<int:pk>/', UpdateGroup.as_view(), name='update_group'),
    path('delete/<int:pk>/', DeleteGroup.as_view(), name='delete_group'),
]