from django.contrib import admin
from .models import *
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name' ,'company_type')
    list_filter = ('name' ,'company_type')
    search_fields = ('name' ,'company_type')
    list_per_page = 15
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name' ,'last_name' ,'company')
    list_filter = ('last_name','company')
    search_fields = ('first_name','last_name','company')
    list_per_page = 15

admin.site.register(Company ,CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
