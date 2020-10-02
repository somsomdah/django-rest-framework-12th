from django.contrib.auth import forms

from .models import User


class UserCreationForm(forms.UserCreationForm):

    class Meta(forms.UserCreationForm):
        model = User
        fields = ('code',)


class UserChangeForm(forms.UserChangeForm):

    class Meta:
        model = User
        fields = ('code',)