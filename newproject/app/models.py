from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    attendence = models.CharField(max_length=100,null=True)
    

class Faculty(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=100)

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

class user_data(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()