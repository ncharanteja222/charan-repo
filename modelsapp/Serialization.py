from rest_framework import serializers
from .models import *
<<<<<<< HEAD

=======
>>>>>>> 051b671bfd7b2c8382ec78ac6b92a48109c6b045


class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

