from django.urls import path
from accounts.views import (index, show, create, edit, delete,profile, login, register, activate)
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    # Dashboard
    path('accounts/index', login_required(index), name='accounts.index'),
    path('accounts/create', login_required(create), name='accounts.create'),
    path('accounts/<int:id>/show', login_required(show), name='accounts.show'),
    path('accounts/<int:id>/edit', login_required(edit), name='accounts.edit'),
    path('accounts/<int:id>/delete', login_required(delete), name='accounts.delete'),

    # Required after login redirect on profile by default
    path('accounts/profile/', profile, name='accounts.profile'),

    # Apis
    path('api/login/', login, name='api.login'),
    # path('api/token/', TokenObtainPairView.as_view(), name='login'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register, name='api.register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'),
    path('api/profile/', profile, name='api.profile'),
]

