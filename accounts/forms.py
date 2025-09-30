from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

# تنسيق Bootstrap موحد
attrs = {'class': 'form-control'}

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=attrs))


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs=attrs))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs=attrs))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=attrs))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs=attrs))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileForm(UserChangeForm):
    password = None  # نخفي حقل الباسورد

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }
