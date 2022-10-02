# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 150)
    manager = models.CharField(max_length = 100)
    number_of_employees = models.IntegerField()
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    email = models.EmailField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name