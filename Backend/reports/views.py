from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReportForm

from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from django.contrib.contenttypes.models import ContentType
from .models import Report
from .serializer import ReportSerializer
from rest_framework.response import Response
from django.core.paginator import Paginator


class ReportList(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    pagination_class = PageNumberPagination

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        content_type_name = request.data.get('content_type')

        if content_type_name:
            try:
                content_type = ContentType.objects.get(model=content_type_name)
            except ContentType.DoesNotExist:
                return Response({'error': f'Content type "{content_type_name}" does not exist'}, status=status.HTTP_400_BAD_REQUEST)

            content_type_id = content_type.id
            request.data['content_type'] = content_type_id
        else:
            return Response({'error': 'Content type not provided in request'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            report = self.get_object()
            content_object = report.content_object  # Retrieve the related object
            if report.content_type.model == 'project':
                return Response(
                    {
                        'title': report.content_object.title,
                        'description': report.content_object.description,
                        'status': report.content_object.status,
                        'created_at': report.content_object.created_at,
                        'updated_at': report.content_object.updated_at,
                        'user_id': report.content_object.user_id,
                        'category_id': report.content_object.category_id,
                        'total_target': report.content_object.total_target,
                        'total_collected': report.content_object.total_collected,
                        'deadline': report.content_object.deadline,
                    }
                )
            elif report.content_type.model == 'comment':
                return Response(
                    {
                        'comment': report.content_object.comment,
                        'project_id': report.content_object.project_id,
                        'user_id': report.content_object.user_id,
                        'created_at': report.content_object.created_at,
                    }
                )
            else:
                return Response({'error': 'Invalid content type'}, status=status.HTTP_400_BAD_REQUEST)
        except Report.DoesNotExist:
            return Response({'error': 'Report not found'}, status=status.HTTP_404_NOT_FOUND)


######################### DashBoard ##################################

def home(request):
    reports = Report.objects.all().order_by('-created_at')
    paginator = Paginator(reports, per_page=10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'reports/index.html', context={'reports': page_obj})


def create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a page displaying all reports
            return redirect('report-home')
    else:
        form = ReportForm()
    return render(request, 'reports/create.html', {'form': form})

# def edit(request, pk=None):
#     instance = None
#     if pk:
#         instance = Report.objects.get(pk=pk)
#     report = Report.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ReportForm(request.POST, instance=report)
#         if form.is_valid():
#             form.save()
#             return redirect('report-home')  # Redirect to a page displaying all reports
#     else:
#         form = ReportForm(instance=report)
#     return render(request, 'reports/create.html', {'form': form ,'instance': instance})


def delete(request, pk):
    report = Report.objects.get(pk=pk)
    report.delete()
    return redirect('report-home')
