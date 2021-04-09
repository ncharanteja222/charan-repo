from django.contrib import admin
from modelsapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','num','roll_num','college_name']
admin.site.register(Student,StudentAdmin)