from django.urls import path
from accounts.views import (index, show, create, edit, delete, login, register, activate)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Dashboard
    path('index', login_required(index), name='accounts.index'),
    path('create', login_required(create), name='accounts.create'),
    path('<int:id>/show', login_required(show), name='accounts.show'),
    path('<int:id>/edit', login_required(edit), name='accounts.edit'),
    path('<int:id>/delete', login_required(delete), name='accounts.delete'),

    # Apis
    path('login/', login.as_view(), name='api.login'),
    path('register/', register, name='api.register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'),
]

