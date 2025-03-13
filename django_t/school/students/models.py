from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField(null=True)


class Teacher(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField(null=False)