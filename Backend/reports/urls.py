from django.urls import path
from .views import ReportList ,home,create,delete,show
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

#user_passes_test(lambda user: user.is_superuser)(login_required(delete))

urlpatterns = [
    path('', ReportList.as_view({'get':'list'}), name='api-report-list'),
    path('create',ReportList.as_view({'post':'create'}), name='api-report-create'),
    path('<int:pk>/', ReportList.as_view({'get': 'retrieve'}), name='api-report-detail'),
    
    path('home/', user_passes_test(lambda user: user.is_superuser)(login_required(home)), name='report-home'),
    
    path('create/', user_passes_test(lambda user: user.is_superuser)(login_required(create)), name='reports-create'),
    
    path('<int:pk>/delete', user_passes_test(lambda user: user.is_superuser)(login_required(delete)), name='reports-delete'),
    
    path('<int:id>/show',show,name="reports-show")
]