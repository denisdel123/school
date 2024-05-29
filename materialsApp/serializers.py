from rest_framework import serializers

from materialsApp.models import Course, Lesson, Subscription
from materialsApp.validators import youtube_url_validator

"""Сериализатор для ViewSet контроллера """


class LessonSerializer(serializers.ModelSerializer):
    url_to_video = serializers.URLField(validators=[youtube_url_validator])

    class Meta:
        model = Lesson
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'course']


class CourseSerializer(serializers.ModelSerializer):
    num_lesson = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(source='lesson_course', many=True, read_only=True, )
    sub = SubscriptionSerializer(source='sub_course', many=True, read_only=True, )

    class Meta:
        model = Course
        fields = "__all__"

    def get_num_lesson(self, obj):
        return Lesson.objects.filter(course=obj).count()
