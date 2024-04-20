from django.urls import path
from payments.views import PaymentViewSet,payments_index,payment_show,payments_create

urlpatterns = [
    path('create/', PaymentViewSet.as_view({'post': 'create'}), name='createPayment'),
    path('show/<int:id>', PaymentViewSet.as_view({'get': 'show'}), name='showPayment'),
    path('list/', PaymentViewSet.as_view({'get': 'list'}), name='listByProject'),
    path('listByProject/<int:id>', PaymentViewSet.as_view({'get': 'list_by_project'}), name='listByProject'),
    path('listByUser/<int:id>', PaymentViewSet.as_view({'get': 'list_by_user'}), name='listByUser'),
    path('index/',payments_index,name="paymentsindex"),
    path('showone/<int:id>',payment_show,name="paymentsshow"),
    path('create',payments_create,name="paymentscreate"),
    
]