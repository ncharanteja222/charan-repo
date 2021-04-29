from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serialization import Student_serializer

@api_view(['GET', 'POST'])
def create_view(request):
    if request.method == 'GET':
        s = Student.objects.all()
        print(s)

        Es = Student_serializer(s, many=True)
        print(Es.data)
        return Response(Es.data)
    elif request.method == 'POST':
        d = request.data
        s = Student_serializer(data=d)
        if s.is_valid():
            s.save()
            return Response('success')

#
def js_view(request):
    x = {
      "name": "John",
      "age": 30,
      "city": "New York",
   }

    print(x)
    y = json.dumps(x)
    return HttpResponse(y)



