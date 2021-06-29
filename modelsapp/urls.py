# from django.conf.urls import url
from django.urls import path
from .import views
urlpatterns = [
    path('getall/',views.student_list),
    path('getstu/<int:id>',views.student_list),
    path('create/',views.student_create),
    path('modified/<int:id>',views.student_update),
    path('delete/<int:id>',views.student_delete),

]



