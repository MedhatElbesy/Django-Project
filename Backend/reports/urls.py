from django.urls import path
from .views import ReportList

urlpatterns = [
    path('', ReportList.as_view({'get':'list'}), name='report-list'),
    path('create',ReportList.as_view({'post':'create'}), name='report-create'),
    path('<int:pk>/', ReportList.as_view({'get': 'retrieve'}), name='report-detail'),
]