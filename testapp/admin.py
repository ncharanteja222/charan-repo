from django.contrib import admin
from testapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['emp_name','emp_num','emp_details','emp_address']
admin.site.register(Employee,EmployeeAdmin)

# Register your models here.
