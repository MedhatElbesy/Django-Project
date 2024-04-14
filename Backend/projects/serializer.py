# serializer for project
from rest_framework import serializers
from .models import Project



class ProjectSerializer(serializers.ModelSerializer):

    pictures_url = serializers.SerializerMethodField()
    class Meta:
        model = Project
        exclude=['is_deleted', 'total_collected', 'deleted_at']
        

    def get_pictures_url(self, obj):
        request = self.context.get('request')
        if obj.pictures:
            return request.build_absolute_uri(obj.pictures.url)
        return None
