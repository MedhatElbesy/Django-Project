from django import forms
from tags.models import Tags

class TagForm(forms.Form):
    name = forms.CharField(max_length=100,label=' Name', required=True)
  

class TagModelForm(forms.ModelForm):
  class Meta:
    model = Tags
    fields = '__all__'