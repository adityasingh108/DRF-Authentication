from rest_framework import viewsets
from . models import Student
from .serializers import StudentSerializers
from .Authentication import CustomAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class StudenetModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  # Set the permission

