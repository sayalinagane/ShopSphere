from django import forms
from .models import Order
from .models import Contact

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'city', 'zip_code', 'payment_method']
        widgets = {
            'payment_method': forms.RadioSelect
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']