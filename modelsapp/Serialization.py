from rest_framework import serializers
from .models import *
# import json


class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
