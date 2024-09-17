"""
Формы для управления пользователями
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    Форма авторизации
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Логин",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Пароль",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    """
    Форма регистрации
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Логин",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Почта",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Пароль",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Пароль (повторно)",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
