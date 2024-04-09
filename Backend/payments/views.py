from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.http import HttpResponse
from payments.models import Payment
from payments.forms import PaymentModelForm
import json


# Create your views here.
def all_payments(request):
    payment = Payment.objects.all()
    return render(request,template_name="payment/index.html",
                context={"allPayments":payment})


def payment_show(request,id):
    payment = get_object_or_404(Payment,pk=id)
    return render(request,template_name="payment/show.html",
                context={"onePayment":payment})


def create_payment(request):
    form = PaymentModelForm()
    if request.method == "POST":
        form = PaymentModelForm(request.POST)
        if form.is_valid():
            payment = form.save()
            return redirect(payment.show_url)
    return render(request , template_name="payment/forms/paymentForm.html"
                    ,context={"form":form})