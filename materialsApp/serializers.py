from rest_framework import serializers

from materialsApp.models import Course, Lesson

"""Сериализатор для ViewSet контроллера """


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


"""Сериализатор для generics контроллеров """


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
