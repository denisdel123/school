from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from usersApp.models import Payments
from usersApp.serializers import PaymentsSerializers


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializers


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'method_paid')
    ordering_fields = ('at_payment',)


class PaymentsRetrieverAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    queryset = Payments.objects.all()
