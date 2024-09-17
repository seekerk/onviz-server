"""
Маршруты админки системы
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_view, name="users.login"),
    path('register/', register_user, name="users.register"),
    path("logout/", LogoutView.as_view(), name="users.logout")
]
