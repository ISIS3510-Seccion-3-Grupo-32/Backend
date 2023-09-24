from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.UserLogin.as_view(), name='login'),
    path('register_user/', views.UserRegister.as_view(), name='register'),
    path('logout_user/', views.UserLogout.as_view(), name='logout'),
    path('user/', views.UserView.as_view(), name='user'),
]