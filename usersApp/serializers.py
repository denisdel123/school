from rest_framework import serializers

from usersApp.models import User, Payments

"""Сериализатор для контроллера UserViewSet"""


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserOwnerSerializers(serializers.ModelSerializer):
    payment = PaymentsSerializers(source='user_p', many=True)

    class Meta:
        model = User
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'email', 'groups']


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'email', 'groups']
