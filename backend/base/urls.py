from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BaseIntViewSet, BaseUUIDViewSet

router = DefaultRouter()
router.register(r'base-int', BaseIntViewSet)
router.register(r'base-uuid', BaseUUIDViewSet)

urlpatterns = [
    path('', include(router.urls))
]
