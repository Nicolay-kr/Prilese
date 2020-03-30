from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone', 'customer_email',
                  'customer_address', 'comments',
                  ]

        # widgets = {
        #     'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'customer_phone': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'customer_address': forms.TextInput(attrs={'class': 'form-control'}),
        #     'comments': forms.TextInput(attrs={'class': 'form-control'}),
        #
        # }