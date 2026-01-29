from django.db import models

class Company(models.Model):
   name = models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   industry = models.CharField(max_length=100)
   def __str__(self):
       return self.name

class Employee(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField(unique=True)
   designation = models.CharField(max_length=100)
   salary = models.IntegerField()
   company = models.ForeignKey(
   Company,on_delete=models.CASCADE)
   def __str__(self):
      return self.name
