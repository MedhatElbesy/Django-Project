from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ['id', 'user', 'title', 'description', 'status', 'category', 'tags', 'pictures', 'video',
                  'total_target', 'total_collected', 'deadline', 'is_active', 'is_featured', 'is_deleted',
                  'created_at', 'updated_at', 'deleted_at']
