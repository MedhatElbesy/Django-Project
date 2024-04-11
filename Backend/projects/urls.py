from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
# Default django router
# Dear colleagues it automaticaly creates routes for every function,
# dependingg on the action like /projects/get

router = DefaultRouter()
router.register(r'', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]
