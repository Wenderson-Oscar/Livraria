from django.urls import path
from bookstore.apps.publishers.views.permissions import AddUserGroup, RemoveUserGroup, UpdateNameGroup, AddAdminGroup, RemoveAdminGroup, AskedParticipateEmailGroup

app_name = 'permissions'

urlpatterns = [
    path('add_admin_group/<int:pk>/', AddAdminGroup.as_view(), name='add_admin_group'),
    path('add_user_group/<int:pk>/', AddUserGroup.as_view(), name='add_user_group'),
    path('remove_admin_group/<int:pk>/', RemoveAdminGroup.as_view(), name='remove_admin_group'),
    path('remove_user_group/<int:pk>/<int:pk1>/', RemoveUserGroup.as_view(), name='remove_user_group'),
    path('update_name_group/<int:pk>/', UpdateNameGroup.as_view(), name='update_name_group'),
    path('asked_participate_email_group/', AskedParticipateEmailGroup.as_view(), name='asked_participate_email_group'),
]