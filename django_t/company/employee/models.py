from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length = 256)
    desc = models.TextField(max_length=1024)
    
class Employee(models.Model):
    name = models.CharField(max_length = 256)
    Department = models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
    age = models.IntegerField(null=True)


    