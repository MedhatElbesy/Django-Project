from django.urls import path
from categories.views import CategoryViewSet, index, category_show, category_delete, category_create, category_update
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('create/', CategoryViewSet.as_view({'post': 'create'}), name='create_category'),
    path('show/<int:id>', CategoryViewSet.as_view({'get': 'show'}), name='show_category'),
    path('list/', CategoryViewSet.as_view({'get': 'list'}), name='list_all_categories'),
    path('update/<int:pk>', CategoryViewSet.as_view({'put': 'update'}), name='update_category'),
    path('delete/<int:pk>', CategoryViewSet.as_view({'delete': 'delete'}), name='delete_category'),

    #  Dasboard
    path('home/', user_passes_test(lambda user: user.is_superuser)(login_required(index)),  name='category-home'),

    path('createcategory/', user_passes_test(lambda user: user.is_superuser)(login_required(category_create)),  name='category-create'),

    path('updatecategory/<int:id>', user_passes_test(lambda user: user.is_superuser)(login_required(category_update)),  name='category-update'),

    path('showcategory/<int:id>', user_passes_test(lambda user: user.is_superuser)(login_required(category_show)),  name='category-show'),

    path('deletecategory/<int:id>', user_passes_test(lambda user: user.is_superuser)(login_required(category_delete)),  name='category-delete'),
]