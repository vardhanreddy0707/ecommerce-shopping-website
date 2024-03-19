from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class QuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')