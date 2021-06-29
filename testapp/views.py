from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# from django.http import JsonResponse
# # from testapp.mixin import httpresponsemixin
from rest_framework.response import Response
from testapp.models import Employee
from testapp import serializers

#
class Testviewset(ModelViewSet):
     def retreive(self, request, id=None, *args, **kwargs):
        if id is None:
            emp_data = Employee.objects.all()
            ser=serializers.Employee_serializer(emp_data,many=True)
            return Response(ser.data)
        try:
            emp_data = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            print('the  request source is not availbale')
        ser = serializers.Employee_serializer(emp_data)
        return Response(ser.data)
     def post(self,request):
         ser=serializers.Employee_serializer(data=request.data)
         if ser.is_valid():
             ser.save()
             return Response(ser.data,status='200')
         return Response(ser.data, status=400)

     def patch(self, request, id):
         emp_data = Employee.objects.get(id=id)
         req_data = request.data.get("emp_name" ,'emp_details')
         data={
             "emp_name":req_data
         }
         ser = serializers.Employee_serializer(emp_data, data=data, partial=True)
         if ser.is_valid():
             ser.save()
             return Response(ser.data)
         # return a meaningful error response
         return Response('record was updated partially')

     def put(self, request, id):
         emp_data = Employee.objects.get(id=id)
         print(request.data)
         ser = serializers.Employee_serializer(emp_data, data=request.data)
         if ser.is_valid():
             ser.save()
         return Response(ser.data)

     def delete(self,request,id):
         emp_data=Employee.objects.get(id=id)
         emp_data.delete()
         return Response('successfully deleted')



