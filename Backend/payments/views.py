
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import PaymentSerializer
from .models import Payment

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
