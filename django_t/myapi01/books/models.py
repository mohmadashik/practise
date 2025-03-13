from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13,unique=True)

    def __str__(self):
        return self.title


from django.db import models 
class Department(models.Model):
    title=  models.CharField(max_length=100)
class User(models.Model):
    name = models.CharField(max_length=500)
    department = models.Foreigkey(Department,on_delete=models.CASCADE)
class Manager(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
