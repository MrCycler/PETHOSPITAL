# Django urls library
from django.urls import include, path
# DRF urls library
from rest_framework.routers import DefaultRouter

# Import of views & viewsets
from .views import ClientViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash=False)
router.register('clients',ClientViewSet,'ClientViewSet')

# URL patterns
urlpatterns = [
    path('', include(router.urls)),
]