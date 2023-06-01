from reader import views
from django.urls import path


urlpatterns = [
    path('create/new/', views.CreateReader.as_view(), name='create_reader'),
    path('login/user/', views.Login.as_view(), name='login_user'),
    path('logout/user/', views.Logout.as_view(), name='logout_user'),
]