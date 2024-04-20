from rest_framework import serializers
from projects.serializer import ProjectSerializer
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    # project = ProjectSerializer()
    class Meta:
        model = Rating
        fields = '__all__'
