from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from .CustomToken import CustomAuthToken

router = DefaultRouter()
router.register('student', views.StudenetModelViewSet, basename='Student')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomAuthToken.as_view()),
]
