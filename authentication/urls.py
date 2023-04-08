from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.api import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
print("test")
urlpatterns = [
    path('', include(router.urls)),
]
