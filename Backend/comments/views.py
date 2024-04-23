from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializer import CommentSerializer
from django.contrib import messages
from .forms import CommentForm
# Create your views here.


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def get_project_comment(self, request, project_id):
        queryset = Comment.objects.filter(project_id=project_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    # @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    @api_view(['POST'])
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


def delete_comment(request, id):
    comment = Comment.objects.get(pk=id)
    messages.success(request, 'Comment is deleted Succufuly')
    comment.delete()
    return redirect('project.comments', comment.project_id)


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            messages.success(request, 'Comment is Create Succufuly')
            return redirect('project.comments', comment.project_id)
    else:
        form = CommentForm()
    return render(request, 'create.html', {'form': form})
