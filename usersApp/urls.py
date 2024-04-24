from django.urls import path
from rest_framework.routers import DefaultRouter

from usersApp.apps import UsersappConfig
from usersApp.views import UserViewSet

app_name = UsersappConfig.name
router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')

urlpatterns = [

]

urlpatterns += router.urls
