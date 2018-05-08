from django import forms
from app.models import users
from django.contrib.auth.models import User
class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=("username","email","password")

class userformother(forms.ModelForm):
    class Meta():
        model=users
        fields=("portfolio","image")
