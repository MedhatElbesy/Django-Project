from django.urls import path
from accounts.views import (index, show, create, edit, delete)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Dashboard
    path('index', login_required(index), name='accounts.index'),
    path('create', login_required(create), name='accounts.create'),
    path('<int:id>/show', login_required(show), name='accounts.show'),
    path('<int:id>/edit', login_required(edit), name='accounts.edit'),
    path('<int:id>/delete', login_required(delete), name='accounts.delete'),

    # Apis

]

