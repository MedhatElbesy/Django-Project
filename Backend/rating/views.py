from django.shortcuts import redirect ,render
from rest_framework.exceptions import ValidationError
from django.db.models import Avg
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Rating
from projects.models import Project
from projects.serializer import ProjectSerializer
from .serializers import RatingSerializer
from .forms import RatingForm
from django.contrib import messages


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    # @action(detail=False, methods=['post'])
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        top_projects = Project.objects.filter(is_active=True).annotate(
            avg_rating=Avg('ratings__rating')).order_by('-avg_rating')[:5]
        serializer = ProjectSerializer(top_projects, many=True)
        return Response(serializer.data)


def create_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save()
            messages.success(request, 'Rating is Create Succufuly')
            return redirect('project.rating' ,rating.project_id)  
    else:
        form = RatingForm()
    return render(request, 'create.html', {'form': form})

def delete_rating(request,id):
    rating = Rating.objects.get(id=id)
    rating.delete()
    messages.success(request, 'Rating is Delete Succufuly')
    return redirect('project.rating' ,rating.project_id)