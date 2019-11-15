from django.shortcuts import render
from .models import employee
from .serializers import employee_serializer
from rest_framework import generics

# Create your views here.
class create_list(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employee_serializer
    class UPDATE_DETEL_RETRIVE(generics.RetrieveUpdateDestroyAPIView):
        queryset = employee.objects.all()
        serializer_class = employee_serializer
class UPDATE_DETEL_RETRIVE(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employee_serializer