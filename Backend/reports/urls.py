from django.urls import path
from .views import ReportList ,home,create,delete

urlpatterns = [
    path('', ReportList.as_view({'get':'list'}), name='api-report-list'),
    path('create',ReportList.as_view({'post':'create'}), name='api-report-create'),
    path('<int:pk>/', ReportList.as_view({'get': 'retrieve'}), name='api-report-detail'),
    path('home/', home, name='report-home'),
    path('create', create, name='reports-create'),
    path('<int:pk>/delete', delete, name='reports-delete'),
]