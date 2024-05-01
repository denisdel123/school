from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from usersApp.apps import UsersappConfig
from usersApp.views.payments import PaymentsCreateAPIView, PaymentsListAPIView, PaymentsRetrieverAPIView, \
    PaymentsUpdateAPIView, PaymentsDestroyAPIView
from usersApp.views.user import UserViewSet

app_name = UsersappConfig.name

# router for users model
router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    # urls payment
    path('payment/create/', PaymentsCreateAPIView.as_view(), name='payment_create'),
    path('payment/', PaymentsListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>', PaymentsRetrieverAPIView.as_view(), name='payment_retriever'),
    path('payment/destroy/', PaymentsUpdateAPIView.as_view(), name='payment_update'),
    path('payment/destroy/', PaymentsDestroyAPIView.as_view(), name='payment_destroy'),

    # urls token
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='access_token'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

]

urlpatterns += router.urls
