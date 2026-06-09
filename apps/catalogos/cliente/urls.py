from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteModelViewSet

router = DefaultRouter()

router.register('', ClienteModelViewSet, basename='cliente')


urlpatterns = [
    path('', include(router.urls)),
]