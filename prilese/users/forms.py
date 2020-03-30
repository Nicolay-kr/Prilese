from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2',
                  ]

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password2': forms.TextInput(attrs={'class': 'form-control'}),
        # }