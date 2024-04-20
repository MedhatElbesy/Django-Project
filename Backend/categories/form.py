from django import forms
from categories.models import Category

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100,label=' Name', required=True)
    description = forms.CharField(max_length=100,label=' description', required=True)
  

class CategoryModelForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'