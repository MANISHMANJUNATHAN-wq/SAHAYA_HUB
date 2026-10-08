from django import forms
from .models import HelpRequest

class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['title', 'category', 'location', 'contact_name', 'contact_phone', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Need O+ Blood Donor'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Vijayanagar'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Details...'}),
        }