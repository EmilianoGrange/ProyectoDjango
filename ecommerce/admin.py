from django.contrib import admin
from .models import Product, Employee, Supplier

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category', 'price']
#     search_fields = ['title', 'category', 'price']
#    list_filter = ['title', 'category', 'price']

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['last_name', 'position', 'salary']
#     search_fields = ['last_name', 'position', 'email']
#    list_filter = [['last_name', 'position', 'salary']]

# class SupplierAdmin(admin.ModelAdmin):
#     list_display = ['last_name', 'email']
#     search_fields = ['last_name', 'email']
#    list_filter = ['last_name', 'email']

# Register your models here.
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Supplier)