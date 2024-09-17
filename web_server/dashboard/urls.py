"""
Маршруты к дашбоарду
"""

from django.urls import path

from web_server.dashboard.views import dashboard_view

urlpatterns = [
    path('', dashboard_view, name="dashboard"),
]
