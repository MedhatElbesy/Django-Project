from django import forms
from projects.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','deadline','user','category','tags','pictures','total_target']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 2, 'cols': 2}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Deadline', 'type': 'date'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'pictures': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'total_target': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Target'}),
        }

        