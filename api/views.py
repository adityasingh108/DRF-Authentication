from rest_framework import viewsets 
from . models import Student
from .serializers import StudentSerializers
from rest_framework.authentication import BasicAuthentication ,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custumPermission import MyPermission
# Create your views here.

class StudenetModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers 
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly ,IsAuthenticated,AllowAny,DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoModelPermissions]
    permission_classes  = [MyPermission]