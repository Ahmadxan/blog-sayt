from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from accounts.models import CustomUser
from post.models import Contact


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    widgets = {
        'name': forms.TextInput(
            attrs={
                'class': "form-control"
            }
        ),
        'phone': forms.TextInput(
            attrs={
                'class': "form-control"
            }
        ),
        'email': forms.TextInput(
            attrs={
                'class': "form-control"
            }
        ),
        'message': forms.TextInput(
            attrs={
                'class': "form-control"
            }
        ),
    }