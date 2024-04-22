from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['rating', 'user', 'project']
        #style bs 5
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
            'project': forms.Select(attrs={'class': 'form-select'}),
        }
