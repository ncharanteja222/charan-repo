from django.contrib import admin
from django.urls import path, include
# from modelsapp import views
from .import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('test-viewset',views.Testviewset,basename='test-viewset')

urlpatterns = [
    path('',include(router.urls)),
    # path('getemp/<int:id>',views.Testviewset.as_view()),
    # path('gettingall/',views.Testviewset.as_view()),
    # path('getall/',views.student_list),
    # path('getstu/<int:id>',views.student_list),
    # path('create/',views.student_create),
    # path('modified/<int:id>',views.student_update),
    # path('delete/<int:id>',views.student_delete)
]
