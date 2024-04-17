from django.urls import path
from .views import home ,create,delete


urlpatterns = [
    path('', home, name='report-home'),
    path('create/', create, name='reports-create'),
    #path('<int:pk>/edit', edit, name='reports-edit'),
    path('<int:pk>/delete/', delete, name='reports-delete'),
]


