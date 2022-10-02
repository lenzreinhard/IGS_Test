# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from CRUD.models import Employee
from CRUD.models import Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)