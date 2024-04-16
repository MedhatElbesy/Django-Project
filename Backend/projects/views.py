# from django.shortcuts import render
from rest_framework.exceptions import ValidationError
import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Project, ProjectStatus
from .serializer import ProjectSerializer
from datetime import datetime, timedelta
from rest_framework.exceptions import ValidationError


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    from datetime import datetime, timedelta

    def create(self, request, *args, **kwargs):
        try:
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                # check if date is at least more than a week ahead
                deadline = serializer.validated_data.get('deadline')
                if deadline < datetime.now().date() + timedelta(days=7):
                    return Response({'error': 'End date must be at least a week ahead'}, status=status.HTTP_400_BAD_REQUEST)

                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = ProjectSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # delete single project
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def read(self, request, *args, **kwargs):
        try:
            project = Project.objects.get(id=kwargs['pk'])
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        try:
            projects = Project.objects.all()
            serializer = ProjectSerializer(
                projects, many=True, context={'request': request})
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({'error': 'No projects found'}, status=status.HTTP_404_NOT_FOUND)

    # Additional custom methods can be added here
    @action(detail=False, methods=['get'])
    def featured(self, request, *args, **kwargs):
        try:
            projects = Project.objects.filter(is_featured=True)
            serializer = ProjectSerializer(
                projects, many=True, context={'request': request})
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({'error': 'No featured projects found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def latest(self, request, *args, **kwargs):
        projects = Project.objects.order_by('-created_at')[:10]
        serializer = ProjectSerializer(
            projects, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def change_status(self, request, *args, **kwargs):
        try:
            project = Project.objects.get(id=kwargs['pk'])
            current_status = project.status
            # status toggler
            new_status = ProjectStatus.IN_PROGRESS if current_status == ProjectStatus.DONE else ProjectStatus.DONE
            project.status = new_status
            project.save()
            return Response({'status': f"Project status changed to {new_status}"}, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

    # TODO after donation implementation
    # def get_project_donations(self, request, *args, **kwargs):
    #     try:
    #         project = Project.objects.get(id=kwargs['pk'])
    #         donations = project.donations.all()
    #         serializer = DonationSerializer(donations, many=True)
    #         return Response(serializer.data)
    #     except Project.DoesNotExist:
    #         return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
