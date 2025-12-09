from django import forms

from .models import ConsultationRequest


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام شما'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل شما'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تلفن (اختیاری)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'پیام شما'}),
        }