from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=30, null=True)
    emp_num= models.IntegerField(null=True)
    emp_details=models.CharField(max_length=60, null=True)
    emp_address=models.CharField(max_length=50, null=True)
