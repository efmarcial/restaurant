from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from user.models import UserProfile
from django.forms import TextInput, EmailInput, Select, FileInput


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name', widget=forms.TextInput(attrs={'class': "bo-rad-10 sizefull txt10 p-l-20"}))
    email = forms.EmailField(max_length=200, label='E-mail', widget=forms.TextInput(attrs={'class': "bo-rad-10 sizefull txt10 p-l-20"}))
    first_name = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(attrs={'class': "bo-rad-10 sizefull txt10 p-l-20"}))
    last_name = forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(attrs={'class': "bo-rad-10 sizefull txt10 p-l-20"}))
    password1 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput(attrs={'class': "bo-rad-10 sizefull txt10 p-l-20"}))
    password2 = forms.CharField(max_length=100, label='Password Confirmation', widget=forms.PasswordInput(attrs={'class': "bo-rad-10 sizefull txt10 p-l-20"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        widgets = {
            'username': TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'placeholder': 'last_name'}),
            'password': TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'value': 'aa'}),
        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('New York', 'New York'),
    ('Tokyo', 'Tokyo'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20 p-t-10', 'placeholder': 'image', }),
        }