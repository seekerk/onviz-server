"""
Обработка запросов к дашбоарду
"""
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render


def dashboard_view(request: HttpRequest) -> HttpResponse:
    """
    Отрисовка дашбоарда
    """
    if not request.user.is_authenticated:
        return redirect("users.login")

    return render(request, "dashboard/dashboard.html")
