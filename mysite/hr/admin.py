from django.contrib import admin
from .models import *
# Register your models here.
class groupmodeladmin(admin.ModelAdmin):
  list_display = ('id', 'groupname', 'created_date', 'updated_at')
#   list_filter = ('created_date','line')
admin.site.register(groupmodel, groupmodeladmin)

class departmentadmin(admin.ModelAdmin):
    list_display = ('id', 'group_name', 'department_name')
admin.site.register(department, departmentadmin)

class genderadmin(admin.ModelAdmin):
    list_display = ('id', 'gendertype')
admin.site.register(gender, genderadmin)

class regionadmin(admin.ModelAdmin):
    list_display = ('id', 'region_name')
admin.site.register(region, regionadmin)

class employeeadmin(admin.ModelAdmin):
    list_display = ('id', 'employee_code', 'employee_eng_name', 'department', 'role')
admin.site.register(employee, employeeadmin)