from django.urls import path
from tags.views import TagsViewSet

urlpatterns = [
    path('create/', TagsViewSet.as_view({'post': 'create'}), name='create_tags'),
    path('show/<int:id>', TagsViewSet.as_view({'get': 'show'}), name='show_tags'),
    path('list/', TagsViewSet.as_view({'get': 'list'}), name='list_all_tags'),
    path('update/<int:pk>', TagsViewSet.as_view({'put': 'update'}), name='update_tags'),
    path('delete/<int:pk>', TagsViewSet.as_view({'delete': 'delete'}), name='delete_tags'),
]