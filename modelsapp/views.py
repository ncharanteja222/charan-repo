from django.http import HttpResponse
from modelsapp.models import Student
# from django.views.generic import View
# from django.core.serializers import serialize
# from modelsapp.mixin import SerializeMixin
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from modelsapp.serializers import Student_serializer

@api_view(['GET'])
def student_list(request,id=None):
    if id is None:
      stu_data=Student.objects.all()
      ser=Student_serializer(stu_data,many=True)
      return Response(ser.data)
    else:
      stu_data = Student.objects.get(id=id)
      ser=Student_serializer(stu_data)
      return Response(ser.data)

@api_view(['POST'])
def student_create(request):
    ser=Student_serializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status=200)
    else:
        return Response(status=400)
@api_view(['PUT'])
def student_update(requrest,id):
    stu_data=Student.objects.get(id=id)
    ser=Student_serializer(stu_data,data=requrest.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response('data updated successfully')

@api_view(['DELETE'])
def student_delete(request,id):
    stu_data=Student.objects.get(id=id)
    stu_data.delete()
    return Response('data deleted successfully')







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





