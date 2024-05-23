from rest_framework import generics

from paymentApp.models import Payment
from paymentApp.serializers import PymentSerializer
from paymentApp.services import convert_rub_to_usd, create_stripe_product, create_stripe_price, create_stripe_session


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(owner=self.request.user)
        amount_in_usd = convert_rub_to_usd(payment.amount)
        product = create_stripe_product(payment.course.name)
        price = create_stripe_price(amount_in_usd, product)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


