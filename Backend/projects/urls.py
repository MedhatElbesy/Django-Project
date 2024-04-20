from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet , index, view_details,soft_delete ,project_deleted,add_to_feature,create_project,edit_project,top_five_rated_projects,five_featured_projects
# Default django router
# Dear colleagues it automaticaly creates routes for every function,
# dependingg on the action like /projects/get

router = DefaultRouter()
router.register(r'', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('home', index, name='project.home'),
    path('<int:pk>/show',view_details,name="project.show"),
    path('<int:id>/delete',soft_delete,name="project.delete"),
    path('deleted',project_deleted,name="project.deleted"),
    path('<int:id>/featured',add_to_feature,name="project.featured"),
    path('create',create_project,name="project.create"),
    path('<int:id>/edit',edit_project,name="project.edit"),
    path('toprated',top_five_rated_projects,name="project.top_rated"),
    path('features',five_featured_projects,name="project.features")
]
