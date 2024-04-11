from django.urls import path
from .views import ReportList

urlpatterns = [
    path('reports/', ReportList.as_view({'get':'list'}), name='report-list'),
]