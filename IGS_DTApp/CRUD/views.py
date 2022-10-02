# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class ListEmployee(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DetailEmployee(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CreateEmployee(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeleteEmployee(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ListDepartment(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DetailDepartment(generics.RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CreateDepartment(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DeleteDepartment(generics.DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


def Employees(request):
    return render(request,'employees.html',{'employees':Employee.objects.all()})

def Departments(request):
    return render(request,'departments.html',{'departments':Department.objects.all()})