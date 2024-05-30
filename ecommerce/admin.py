from django.contrib import admin
from .models import Product, Employee, Supplier

# Register your models here.
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Supplier)