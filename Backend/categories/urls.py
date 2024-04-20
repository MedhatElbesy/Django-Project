from django.urls import path
from categories.views import CategoryViewSet, index, category_show, category_delete, category_create, category_update

urlpatterns = [
    path('create/', CategoryViewSet.as_view({'post': 'create'}), name='create_category'),
    path('show/<int:id>', CategoryViewSet.as_view({'get': 'show'}), name='show_category'),
    path('list/', CategoryViewSet.as_view({'get': 'list'}), name='list_all_categories'),
    path('update/<int:pk>', CategoryViewSet.as_view({'put': 'update'}), name='update_category'),
    path('delete/<int:pk>', CategoryViewSet.as_view({'delete': 'delete'}), name='delete_category'),

    path('index/', index,  name='category_index'),
    path('createcategory/', category_create,  name='category_create'),
    path('updatecategory/<int:id>', category_update,  name='category_update'),
    path('showcategory/<int:id>', category_show,  name='category_show'),
    path('deletecategory/<int:id>', category_delete,  name='category_delete'),
]