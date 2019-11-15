from .models import employee
from rest_framework import serializers
class employee_serializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'