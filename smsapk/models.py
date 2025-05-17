from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()

class Course(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    

class Student(models.model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_lenght=255)
    email=models.CharField(max_lenght=255)
    password=models.CharField(max_lenght=255)
    gender=models.CharField(max_lenght=255)
    profile_pic=models.FileField()
    address=models. TextField()
