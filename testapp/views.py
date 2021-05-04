from django.shortcuts import render
from django.http import HttpResponse
import json

from django.views import View
# from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse
from testapp.mixin import httpresponsemixin


class Emp(httpresponsemixin,View):
    def get(self,request,*args,**kwargs):
        d = {"me":"hi this is the first cbv"}
        emp_data=json.dumps(d)
        print(type(emp_data))
        return self.render_to_httpresponse(emp_data)
    def post(self,request,*args,**kwargs):
        f = json.dumps({"me": "hi this is the post method cbv"})
        return self.render_to_httpresponse(f)

    def put(self,request,*args,**kwargs):
        return HttpResponse('HI thsi is to put')


class Student(APIView):

    def get(self, request, *args, **kwargs):
        emp_data = {"me": "hi this is the fiAPIViewrst cbv"}
        print(type(emp_data))
        return JsonResponse(emp_data)
