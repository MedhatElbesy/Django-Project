# forms.py
from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['content_type', 'object_id','user','reason']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'reason': forms.Select(attrs={'class': 'form-select'}),
        }