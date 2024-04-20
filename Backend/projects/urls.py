from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.decorators import login_required

from .views import ProjectViewSet , index, view_details,soft_delete ,project_deleted,add_to_feature,create_project,edit_project,top_five_rated_projects,five_featured_projects,project_commests


# Default django router
# Dear colleagues it automaticaly creates routes for every function,
# dependingg on the action like /projects/get

router = DefaultRouter()
router.register(r'', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('home', login_required(index), name='project.home'),
    path('<int:pk>/show',login_required(view_details),name="project.show"),
    path('<int:id>/delete',login_required(soft_delete),name="project.delete"),
    path('deleted',login_required(project_deleted),name="project.deleted"),
    path('<int:id>/featured',login_required(add_to_feature),name="project.featured"),
    path('create',login_required(create_project),name="project.create"),
    path('<int:id>/edit',login_required(edit_project),name="project.edit"),
    path('toprated',login_required(top_five_rated_projects),name="project.top_rated"),
    path('features',login_required(five_featured_projects),name="project.features"),
    path('<int:id>/comments',login_required(project_commests),name="project.comments")
]
