from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.decorators import login_required

from .views import ProjectViewSet , index, view_details,soft_delete ,project_deleted,add_to_feature,create_project,edit_project,top_five_rated_projects,five_featured_projects,project_commests,search_projects,get_rating_project

from comments.views import delete_comment ,create_comment
from rating.views import create_rating , delete_rating
from django.contrib.auth.decorators import user_passes_test
# Default django router
# Dear colleagues it automaticaly creates routes for every function,
# dependingg on the action like /projects/get

router = DefaultRouter()
router.register(r'', ProjectViewSet, basename='project')
#user_passes_test(lambda user: user.is_superuser)(login_required(delete_rating))
#five_featured_projects
urlpatterns = [
    path('', include(router.urls)),
    path('home', user_passes_test(lambda user: user.is_superuser)(login_required(index)), name='project.home'),

    path('<int:pk>/show',user_passes_test(lambda user: user.is_superuser)(login_required(view_details)),name="project.show"),

    path('<int:id>/delete',login_required(soft_delete),name="project.delete"),

    path('deleted',user_passes_test(lambda user: user.is_superuser)(login_required(soft_delete)),name="project.deleted"),

    path('<int:id>/featured',user_passes_test(lambda user: user.is_superuser)(login_required(add_to_feature)),name="project.featured"),
    
    path('create',user_passes_test(lambda user: user.is_superuser)(login_required(create_project)),name="project.create"),
    
    path('<int:id>/edit',user_passes_test(lambda user: user.is_superuser)(login_required(edit_project)),name="project.edit"),
    
    path('toprated',user_passes_test(lambda user: user.is_superuser)(login_required(top_five_rated_projects)),name="project.top_rated"),
    
    path('features',user_passes_test(lambda user: user.is_superuser)(login_required(five_featured_projects)),name="project.features"),
    
    path('<int:id>/comments',user_passes_test(lambda user: user.is_superuser)(login_required(project_commests)),name="project.comments"),

    path('search',user_passes_test(lambda user: user.is_superuser)(login_required(search_projects)),name="project.search"),

    path('comments/<int:id>/delete',user_passes_test(lambda user: user.is_superuser)(login_required(delete_comment)),name="project.delete_comment"),

    path('comments/create',user_passes_test(lambda user: user.is_superuser)(login_required(create_comment)),name="project.create_comment"),

    path('<int:id>/rating',user_passes_test(lambda user: user.is_superuser)(login_required(get_rating_project)),name="project.rating"),

    path('rating/create',user_passes_test(lambda user: user.is_superuser)(login_required(create_rating)),name="project.rating_create"),

    path('rating/<int:id>/delete',user_passes_test(lambda user: user.is_superuser)(login_required(delete_rating)),name="project.rating_delete"),
]
