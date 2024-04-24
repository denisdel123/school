from rest_framework import viewsets

from materialsApp.models import Course
from materialsApp.serializers import CourseSerializer

"""Контроллер на основе ViewSet"""


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
