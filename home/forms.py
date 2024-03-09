from django.utils import timezone 
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta :
        model = Contact
        fields = ['name','email','phone_number','message']
        widgets = {
            'message': forms.Textarea(attrs={'cols':30, 'rows': 5})
        }
