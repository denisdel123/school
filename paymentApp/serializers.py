from rest_framework import serializers

from paymentApp.models import Payment


class PymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"
