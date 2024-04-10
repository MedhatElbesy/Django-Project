
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import PaymentSerializer
from .models import Payment

# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def createa(self, request):
        try:
            serializer = PaymentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def show(self, request):
        try:
            payment_id = request.payment_id
            project = Payment.objects.filter(payments_id=payment_id)
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
        

    def list_by_project(self, request):
        try:
            project_id = request.project.id
            payments = Payment.objects.filter(project_id=project_id)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({'error': 'No Payment found'}, status=status.HTTP_404_NOT_FOUND)
        
    
    def list_by_user(self, request):
        try:
            user_id = request.user.id 
            payments = Payment.objects.filter(user_id=user_id)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({'error': 'No Payment found'}, status=status.HTTP_404_NOT_FOUND)