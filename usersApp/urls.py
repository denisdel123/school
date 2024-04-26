from django.urls import path
from rest_framework.routers import DefaultRouter

from usersApp.apps import UsersappConfig
from usersApp.views.payments import PaymentsCreateAPIView, PaymentsListAPIView, PaymentsRetrieverAPIView, \
    PaymentsUpdateAPIView, PaymentsDestroyAPIView
from usersApp.views.user import UserViewSet

app_name = UsersappConfig.name
router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('payment/create/', PaymentsCreateAPIView.as_view(), name='payment_create'),
    path('payment/', PaymentsListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>', PaymentsRetrieverAPIView.as_view(), name='payment_retriever'),
    path('payment/destroy/', PaymentsUpdateAPIView.as_view(), name='payment_update'),
    path('payment/destroy/', PaymentsDestroyAPIView.as_view(), name='payment_destroy'),



]

urlpatterns += router.urls
