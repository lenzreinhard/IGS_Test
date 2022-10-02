from django.urls import path

from .views import *

urlpatterns = [
    path('employee/',ListEmployee.as_view()),
    path('employee/<int:pk>/',DetailEmployee.as_view()),
    path('employee/create',CreateEmployee.as_view()),
    path('employee/delete/<int:pk>/',DeleteEmployee.as_view()),

    path('department/',ListDepartment.as_view()),
    path('department/<int:pk>/',DetailDepartment.as_view()),
    path('department/create',CreateDepartment.as_view()),
    path('department/delete/<int:pk>/',DeleteDepartment.as_view()),
]