from rest_framework import serializers

from materialsApp.models import Course, Lesson

"""Сериализатор для ViewSet контроллера """


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    num_lesson = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(source='course', many=True, read_only=True, )

    class Meta:
        model = Course
        fields = "__all__"

    def get_num_lesson(self, obj):
        return Lesson.objects.filter(course=obj).count()
