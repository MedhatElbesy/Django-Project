# from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Project, ProjectStatus, ProjectImage
from .serializer import ProjectSerializer
from datetime import datetime, timedelta
from rest_framework.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib import messages
from projects.forms import ProjectForm
from comments.models import Comment


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    from datetime import datetime, timedelta

    @permission_classes([IsAuthenticated])
    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error': 'You must be authenticated to make a donation'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            pictures = request.FILES.getlist(
                'images')  # Get list of uploaded images
            print(pictures)
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                # Check if date is at least more than a week ahead
                deadline = serializer.validated_data.get('deadline')
                if deadline < datetime.now().date() + timedelta(days=7):
                    return Response({'error': 'End date must be at least a week ahead'}, status=status.HTTP_400_BAD_REQUEST)
                project = serializer.save()

                # Save each image
                for picture in pictures:
                    ProjectImage.objects.create(project=project, image=picture)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @permission_classes([IsAuthenticated])
    def update(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error': 'You must be authenticated to make a donation'}, status=status.HTTP_401_UNAUTHORIZED)
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
        # not authinticated and same user
        if not request.user.is_authenticated:
            return Response({'error': 'You must be authenticated to make a donation'}, status=status.HTTP_401_UNAUTHORIZED)

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
                projects, many=True)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({'error': 'No projects found'}, status=status.HTTP_404_NOT_FOUND)

    # Additional custom methods can be added here
    @action(detail=False, methods=['get'])
    def featured(self, request, *args, **kwargs):
        try:
            projects = Project.objects.filter(is_featured=True)
            serializer = ProjectSerializer(
                projects, many=True)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({'error': 'No featured projects found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def latest(self, request, *args, **kwargs):
        projects = Project.objects.order_by('-created_at')[:5]
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

    @action(detail=False, methods=['get'])
    def top_rated(self, request, *args, **kwargs):
        top_projects = Project.get_top_five_rated_active_project()
        serializer = ProjectSerializer(top_projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # soft delete

    @action(detail=False, methods=['post'])
    def soft_delete(self, request, *args, **kwargs):
        try:
            project = Project.objects.get(id=kwargs['pk'])
            collected = project.get_total_collected()
            target = project.total_target
            same_user = project.user == request.user
            if (collected*0.25) >= target and same_user:
                return Response({'error': 'Project cannot be deleted because it passed 0.25 the target and not the same user'}, status=status.HTTP_400_BAD_REQUEST)
            project.is_deleted = True
            project.deleted_at = timezone.now()
            project.save()
        except:
            return Response({'message': 'Project deleted successfully'}, status=status.HTTP_200_OK)


##############  Dashboard  ###############

def paginatedPages(request, projects, page=5):
    paginator = Paginator(projects, page)  # Show 5 projects per page
    page_number = request.GET.get('page')
    try:
        paginated_projects = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_projects = paginator.page(1)
    except EmptyPage:
        paginated_projects = paginator.page(paginator.num_pages)
    return paginated_projects


def index(request):
    # Get all projects filter is_delelted =false
    projects = Project.objects.filter(is_deleted=False)
    paginated_projects = paginatedPages(request, projects)
    return render(request, 'index.html', {'projects': paginated_projects})


def five_featured_projects(request):
    projects = Project.objects.filter(is_featured=True)
    paginated_projects = paginatedPages(request, projects)
    return render(request, 'index.html', {'projects': paginated_projects})


def project_commests(request, id):
    project = Project.objects.get(id=id)
    comments = Comment.objects.filter(project=project)
    paginated_comments = paginatedPages(request, comments, 4)
    return render(request, 'comments.html', {'comments': paginated_comments, 'project': project})


def project_deleted(request):
    projects = Project.objects.filter(is_deleted=True)
    paginated_projects = paginatedPages(request, projects)
    return render(request, 'index.html', {'projects': paginated_projects})


def top_five_rated_projects(request):
    top_projects = Project.get_top_five_rated_active_project()
    paginated_projects = paginatedPages(request, top_projects)
    return render(request, 'index.html', {'projects': paginated_projects})


def add_to_feature(request, id):
    project = Project.objects.get(id=id)
    featured_count = Project.objects.filter(is_featured=True).count()

    if project.is_featured:
        project.is_featured = False
        messages.success(request, 'Remove Project From Featured!')
        project.save()
        return redirect('project.home')

    if featured_count < 5:
        project.is_featured = True
        messages.success(request, 'Project Has bean featured!')
    else:
        messages.warning(request, 'You can only feature up to 5 projects.')

    project.save()
    return redirect('project.home')


def view_details(requset, pk):
    project = get_object_or_404(Project, id=pk)
    if project.total_target != 0:
        total_money = int(
            (project.total_collected / project.total_target) * 100)
    else:
        total_money = 0
    return render(requset, 'show.html', {'project': project, 'money': total_money})


def soft_delete(request, id):
    project = get_object_or_404(Project, id=id)
    if project.is_deleted:
        project.is_deleted = False
        messages.success(request, 'Project has been Restore!')
    else:
        project.is_deleted = True
        messages.success(request, 'Project has been Deleted!')
    project.deleted_at = timezone.now()
    project.save()
    return redirect('project.home')


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Has been Created!')
            return redirect('project.home')
    else:
        form = ProjectForm()
    return render(request, 'create.html', {'form': form})


def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Has been Updated!')
            return redirect('project.home')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'create.html', {'form': form})


def search_projects(request):
    query = request.GET.get('query')
    search_by = request.GET.get('search_by')

    if query and search_by:
        if search_by == 'category':
            projects = Project.objects.filter(category__name__icontains=query)
        elif search_by == 'tags':
            projects = Project.objects.filter(tags__name__icontains=query)
        else:
            projects = Project.objects.none()
    else:
        projects = Project.objects.all()

    return render(request, 'index.html', {'projects': projects})


def get_rating_project(request, id):
    project = get_object_or_404(Project, id=id)
    ratings = project.ratings.all()
    return render(request, 'ratings.html', {'ratings': ratings, 'project': project})
