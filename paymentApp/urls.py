from django.urls import path

from paymentApp.apps import PaymentappConfig
from paymentApp.views import PaymentCreateAPIView

app_name = PaymentappConfig.name
urlpatterns = [
    path('', PaymentCreateAPIView.as_view(), name='payment')
]