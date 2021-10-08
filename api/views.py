from rest_framework import viewsets 
from . models import Student
from .serializers import StudentSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudenetModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]