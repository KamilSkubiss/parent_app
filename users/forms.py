from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age',)


class CustomChangeForm(UserChangeForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age',)