from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import PaymentSerializer
from .models import Payment
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from projects.views import paginatedPages
# Create your views here.


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        try:
            serializer = PaymentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def show(self, request, id):
        try:
            project = Payment.objects.get(id=id)
            serializer = PaymentSerializer(project)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        try:
            payment = Payment.objects.all()
            serializer = PaymentSerializer(payment, many=True)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({'error': 'No Payment found'}, status=status.HTTP_404_NOT_FOUND)

    def list_by_project(self, request, id):
        try:
            payments = Payment.objects.filter(project=id)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({'error': 'No Payment found'}, status=status.HTTP_404_NOT_FOUND)

    def list_by_user(self, request, id):
        try:
            payments = Payment.objects.get(id=id)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({'error': 'No Payment found'}, status=status.HTTP_404_NOT_FOUND)

def payments_index(request):
    payments = Payment.objects.all()
    paginated_payment = paginatedPages(request, payments)
    return render(request,template_name="payments/crud/index.html",
                context={"payments":paginated_payment})

def payment_show(request,id):
    payments = get_object_or_404(Payment,pk=id)
    return render(request,template_name="payments/crud/show.html",
                context={"payments":payments})

# def payments_create(request):
    if request.method == "POST":
        amount = request.POST("amount")
        currency = request.POST("currency")
        
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValidationError("Amount must be a positive number.")
        except ValueError:
            return JsonResponse({"error": "Invalid amount."}, status=400)
        
        if currency not in ['EUR', 'USD']:
            return JsonResponse({"error": "Invalid currency. Must be EUR or USD."}, status=400)
        payment = Payment(amount=request.POST["amount"],currency=request.POST["currency"],
                    status=request.POST["status"],project_id=request.POST["project_id"],
                    user_id=request.POST["user_id"])
        payment.save()
        return redirect(payment.show_url)
    return render(request,template_name="payments/crud/create.html")





