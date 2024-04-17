from rest_framework import serializers
from .models import Project
from tags.serializer import TagsSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['is_deleted', 'total_collected', 'deleted_at']

    category_name = serializers.CharField(source='category.name', read_only=True)
    tags_info = TagsSerializer(source="tags", many=True, read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    remaining_days = serializers.SerializerMethodField()
    remaining_hours = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    donations = serializers.SerializerMethodField()
    total_collected = serializers.SerializerMethodField()
    get_project_rating = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = "__all__"
        extra_kwargs = {
            'is_deleted': {'write_only': True},
            'is_featured': {'write_only': True},
            'tags': {'write_only': True},
            'category': {'write_only': True},
            'is_active': {'write_only': True},
            # 'user': {'write_only': True},
            'deleted_at': {'write_only': True},
        }

    def get_remaining_days(self, obj):  # Corrected method name
        return obj.get_remaining_days  # Calling the model method

    def get_remaining_hours(self, obj):  # Corrected method name
        return obj.get_remaining_hours  # Calling the model method

    def get_progress(self, obj):
        return obj.get_progress

    def get_donations(self, obj):
        return obj.get_total_payments

    def get_total_collected(self, obj):
        return obj.get_total_collected
