from django.urls import path, re_path
from accounts.views import (index, show, create, edit, delete, admin_profile, profile,update_profile, login, register, activate, forget_password, reset_password)
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,) # type: ignore
from django.contrib.auth.decorators import user_passes_test

urlpatterns = [
     # Dashboard
    path('accounts/index/', user_passes_test(lambda user: user.is_superuser)(login_required(index)),
         name='accounts.index'),
    path('accounts/create/', user_passes_test(lambda user: user.is_superuser)(login_required(create)),
         name='accounts.create'),
    path('accounts/<int:id>/show/', user_passes_test(lambda user: user.is_superuser)(login_required(show)),
         name='accounts.show'),
    path('accounts/<int:id>/edit/', user_passes_test(lambda user: user.is_superuser)(login_required(edit)),
         name='accounts.edit'),
    path('accounts/<int:id>/delete/', user_passes_test(lambda user: user.is_superuser)(login_required(delete)),
         name='accounts.delete'),

    # Required after login redirect on profile by default
    path('accounts/profile/', user_passes_test(lambda user: user.is_superuser)(admin_profile), name='accounts.profile'),

    # Apis
    path('api/login/', login, name='api.login'),
    # path('api/token/', TokenObtainPairView.as_view(), name='login'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register, name='api.register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
    path('api/profile/', profile, name='api.profile'),
    path('api/update_profile/', update_profile, name='api.update_profile'),
    path('api/forget_password/', forget_password, name='api.forget_password'),
    path('api/reset_password/<str:uidb64>/<str:token>/', reset_password, name='api.reset_password'),
]

