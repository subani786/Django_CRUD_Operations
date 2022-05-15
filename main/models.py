from cProfile import label
import email
from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100,verbose_name='User Name',unique=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    re_password=models.CharField(max_length=50,verbose_name='Confirm Password')

    