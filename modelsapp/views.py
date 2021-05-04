from django.shortcuts import render
from django.http import HttpResponse
import json
from modelsapp.models import Student
from django.views.generic import View
# from django.core.serializers import serialize
from modelsapp.mixin import SerializeMixin
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .Serialization import Student_serializer

# @api_view(['GET', 'POST'])
# def create_view(request):
#     if request.method == 'GET':
#         s = Student.objects.all()
#         print(s)
#
#         Es = Student_serializer(s, many=True)
#         print(Es.data)
#         return Response(Es.data)
#     elif request.method == 'POST':
#         d = request.data
#         s = Student_serializer(data=d)
#         if s.is_valid():
#             s.save()
#             return Response('success'.
#             )

class StudentDetailCBV(SerializeMixin,View):
   def get(self,request,id,*args,**kwargs):
       print(id)
       try:
         stu=Student.objects.get(id = id)
       except Student.DoesNotExist:
         y=json.dumps({'msg':'THE REQUEST SOURCE THAT YOU ARE PROVIDED NOT AVAILABLE'})
       else:
       # stu_data ={
       #   "studentname": stu.name,
       #    "num": stu.num,
       #    "roll_num": stu.roll_num,
       #    "college_name": stu.college_name,
       # }
       # print(type(stu_data))
         y = self.Serialize([stu])
       # print(type(y)
       return HttpResponse(y, content_type='application/json')

class StudentListCBV(SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs=Student.objects.all()
        y=self.Serialize(qs)
        return HttpResponse(y, content_type='application/json')












