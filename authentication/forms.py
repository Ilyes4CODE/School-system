from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class register_user(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class login_user(forms.Form):
    username = forms.CharField(
        max_length=342,
    )
    password = forms.CharField(
        widget= forms.PasswordInput(),
        max_length=435,
    )

class prof_registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        