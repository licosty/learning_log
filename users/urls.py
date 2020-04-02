''' Определяет схемы URL для пользователей '''
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # Страница входа
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Страница выхода
    path('logout/', views.logout_view, name='logout'),
    # Страница регистрации
    path('register/', views.register, name='register'),
]