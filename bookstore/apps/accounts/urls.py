from bookstore.apps.accounts import views
from django.urls import path


urlpatterns = [
    path('delete/favority/<int:pk2>/', views.DeleteFavorityBook.as_view(), name='delete_favority'),
    path('create/new/', views.CreateUser.as_view(), name='create_user'),
    path('delete/user/', views.DeleteUser.as_view(), name='delete_user'),
    path('update/user/', views.UpdateUser.as_view(), name='update_user'),
    path('login/user/', views.Login.as_view(), name='login_user'),
    path('logout/user/', views.Logout.as_view(), name='logout_user'),
    path('perfil/', views.PerfilDetail.as_view(), name='perfil'),
    path('password/reset/', views.PasswordChangeUser.as_view(), name='password_reset'),
]