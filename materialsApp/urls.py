from django.urls import path
from rest_framework.routers import DefaultRouter

from materialsApp.apps import MaterialsappConfig
from materialsApp.views.course import CourseViewSet
from materialsApp.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView
from materialsApp.views.subscription import SubscriptionCreate

app_name = MaterialsappConfig.name
router = DefaultRouter()

router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    # model Lesson
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),


    # model Subscription
    path('subscribe/', SubscriptionCreate.as_view(), name='subscribe')

]
# добавление router.urls к ссылкам
urlpatterns += router.urls

