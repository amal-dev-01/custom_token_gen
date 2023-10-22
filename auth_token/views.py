from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from auth_token.models import Student
from auth_token.serializers import StudentSerializer
from rest_framework import viewsets  
from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import 


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication] 
    # permission_classes = [DjangoModelPermissions]
    
