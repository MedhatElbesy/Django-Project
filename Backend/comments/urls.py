from django.urls import path
from .views import CommentViewSet

urlpatterns = [
    path('', CommentViewSet.as_view({'get': 'list'}), name='comment-list'),
    path('project/<int:project_id>',CommentViewSet.as_view({'get': 'get_project_comment'}), name='project-comments'),
    path('create/', CommentViewSet.as_view({'post': 'create'}), name='comment-create'),
    path('<int:pk>/delete',CommentViewSet.as_view({'delete': 'delete'}), name='comment-delete'),
]
