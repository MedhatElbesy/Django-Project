from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RatingViewSet
# Default django router
# Dear colleagues it automaticaly creates routes for every function,
# dependingg on the action like /projects/get

router = DefaultRouter()
router.register(r'', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]
