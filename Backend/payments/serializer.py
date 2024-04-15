from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    project_title = serializers.CharField(
        source='project.title', read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
