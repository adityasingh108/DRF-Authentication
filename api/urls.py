from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from .CustomToken import CustomAuthToken
from rest_framework_simplejwt.views import TokenVerifyView,TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router.register('student', views.StudenetModelViewSet, basename='Student')

urlpatterns = [
    path('', include(router.urls)),
    # path('token/', CustomAuthToken.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('token/verify/',TokenVerifyView.as_view()),
]
