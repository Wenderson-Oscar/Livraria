from bookstore.apps.accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'accounts'

urlpatterns = [
    path('create/new/', views.CreateUser.as_view(), name='create_user'),
    path('delete/user/', views.DeleteUser.as_view(), name='delete_user'),
    path('update/user/', views.UpdateUser.as_view(), name='update_user'),
    path('login/user/', views.Login.as_view(), name='login_user'),
    path('logout/user/', views.Logout.as_view(), name='logout_user'),
    path('perfil/', views.PerfilDetail.as_view(), name='perfil'),
    path('password/reset/', views.PasswordChangeUser.as_view(), name='password_reset'),
    path('recover_password/', views.RecoverPassword.as_view(), name='recover_password'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy("accounts:password_reset_complete"))
        ,name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), 
        name='password_reset_complete'),
]