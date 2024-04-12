from django.urls import path
from categories.views import CategoryViewSet

urlpatterns = [
    path('create/', CategoryViewSet.as_view({'post': 'create'}), name='create_category'),
    path('show/<int:id>', CategoryViewSet.as_view({'get': 'show'}), name='show_category'),
    path('list/', CategoryViewSet.as_view({'get': 'list'}), name='list_all_categories'),
    path('update/<int:pk>', CategoryViewSet.as_view({'put': 'update'}), name='update_category'),
    path('delete/<int:pk>', CategoryViewSet.as_view({'delete': 'delete'}), name='delete_category'),
]