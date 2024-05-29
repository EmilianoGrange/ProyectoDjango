from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Employee, Supplier

# Create your views here.

def home_template(req):
    return render(req, 'home.html', {})

def create_product(req, dict):
    new_product = Product(**dict)
    new_product.save()

    return HttpResponse(f""" <p>Nuevo producto {new_product.title} creado!</p> """)

def show_products(req):
    products = Product.objects.all()

    return render(req, 'products.html', {'products': products})

def show_employees(req):
    employees = Employee.objects.all()

    return render(req, 'employees.html', {'employees': employees})

def show_suppliers(req):
    suppliers = Supplier.objects.all()

    return render(req, 'suppliers.html', {'suppliers': suppliers})