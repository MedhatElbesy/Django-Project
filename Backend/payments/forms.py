from django import forms
from payments.models import Payment

class Payment(forms.Form):
    amount = forms.IntegerField(label='Amount', required=True)
    currency = forms.CharField(label='Currency', required=True)
    status = forms.CharField(label='Status', required=True)


class PaymentModelForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = '__all__'