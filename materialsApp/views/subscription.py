from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from materialsApp.models import Course, Subscription
from materialsApp.serializers import SubscriptionSerializer


class SubscriptionCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course_item = get_object_or_404(Course, id=course_id)

        sub_item = Subscription.objects.all().filter(user=user, course=course_item)

        if sub_item.exists():
            sub_item.delete()
            massage = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            massage = 'Подписка создана'
        return Response({"massage": massage}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        user = request.user
        subscriptions = Subscription.objects.all().filter(user=user)
        serializer = SubscriptionSerializer(subscriptions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
