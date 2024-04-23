from django.urls import path
from tags.views import TagsViewSet, index, tag_show, tag_delete, tag_create, tag_update
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

#user_passes_test(lambda user: user.is_superuser)(login_required(tag_delete))

urlpatterns = [
    path('create/', TagsViewSet.as_view({'post': 'create'}), name='create_tags'),
    path('show/<int:id>', TagsViewSet.as_view({'get': 'show'}), name='show_tags'),
    path('list/', TagsViewSet.as_view({'get': 'list'}), name='list_all_tags'),
    path('update/<int:pk>', TagsViewSet.as_view({'put': 'update'}), name='update_tags'),
    path('delete/<int:pk>', TagsViewSet.as_view({'delete': 'delete'}), name='delete_tags'),

    #dashboard
    path('home/', user_passes_test(lambda user: user.is_superuser)(login_required(index)),  name='tag-home'),

    path('createtag/', user_passes_test(lambda user: user.is_superuser)(login_required(tag_create)),  name='tag-create'),

    path('updatetag/<int:id>', user_passes_test(lambda user: user.is_superuser)(login_required(tag_update)),  name='tag-update'),

    path('showtag/<int:id>', user_passes_test(lambda user: user.is_superuser)(login_required(tag_show)),  name='tag-show'),

    path('deletetag/<int:id>', user_passes_test(lambda user: user.is_superuser)(login_required(tag_delete)),  name='tag-delete'),
]