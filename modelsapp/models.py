from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30,null=True)
    num=models.IntegerField(null=True)
    roll_num=models.IntegerField(null=True)
    college_name=models.CharField(max_length=50, null=True)







