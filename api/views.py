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
    
    
    
 #http POST http://127.0.0.1:8000/api/token/ username="tester" password="passport123"
 #to send post request to the url    