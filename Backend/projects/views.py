# from django.shortcuts import render
from django.shortcuts import render,redirect
from rest_framework.exceptions import ValidationError
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

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    from datetime import datetime, timedelta

    # def create(self, request, *args, **kwargs):
    #     try:
    #         serializer = ProjectSerializer(data=request.data)
    #         if serializer.is_valid():
    #             # check if date is at least more than a week ahead
    #             deadline = serializer.validated_data.get('deadline')
    #             if deadline < datetime.now().date() + timedelta(days=7):
    #                 return Response({'error': 'End date must be at least a week ahead'}, status=status.HTTP_400_BAD_REQUEST)
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except ValidationError as e:
    #         return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def create(self, request, *args, **kwargs):
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
    
    
    
##############  Dashboard  ###############

def paginatedPages(request,projects):
    paginator = Paginator(projects, 5)  # Show 5 projects per page
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


def project_deleted(request):
    projects = Project.objects.filter(is_deleted=True)
    paginated_projects = paginatedPages(request, projects)
    return render(request, 'index.html', {'projects': paginated_projects})

def top_five_rated_projects(request):
    top_projects = Project.get_top_five_rated_active_project()
    paginated_projects = paginatedPages(request, top_projects)
    return render(request, 'index.html', {'projects': paginated_projects})


def add_to_feature(request,id):
    project= Project.objects.get(id=id)
    if project.is_featured:
        project.is_featured=False
        messages.success(request, 'Remove Project From Featured!')
    else:
        project.is_featured=True
        messages.success(request, 'Project Has bean featured!')
    project.save()
    
    return redirect('project.home')

def view_details(requset,pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project)
    if project.total_target != 0:
        total_money= int((project.total_collected / project.total_target) * 100)
    else:
        total_money= 0
    return render(requset,'show.html' , {'project':project , 'money':total_money})


def soft_delete(request,id):
    project = Project.objects.get(id=id)
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
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Has been Created!')
            return redirect('project.home')
    else:
        form = ProjectForm()
    return render(request,'create.html',{'form':form})

def edit_project(request,id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Has been Updated!')
            return redirect('project.home')
    else:
        form = ProjectForm(instance=project)
    return render(request,'create.html',{'form':form})