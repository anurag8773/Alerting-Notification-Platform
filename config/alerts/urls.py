from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TeamViewSet, ProfileViewSet, UserViewSet, AlertViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'alerts', AlertViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
