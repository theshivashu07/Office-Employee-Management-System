
from django.db import models
# Create your models here.


class Roles(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

class Locations(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

class Departments(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Employees(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Departments, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    def __str__(self):
        return "%s %s - %s" %(self.first_name, self.last_name, self.phone)







