"""
Маршруты к компонентам веб сервера
"""

from django.urls import path, include

urlpatterns = [
    path("", include("web_server.users.urls")),  # маршруты для работы фронтом
    path("", include("web_server.dashboard.urls")),
]
