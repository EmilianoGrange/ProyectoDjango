from django.http import HttpResponse
from django.shortcuts import render
from .models import Supplier, Product, Employee
from .forms import SupplierForm, ProductForm, EmployeeForm

# Create your views here.

def home_template(req):
    return render(req, 'home.html', {})

def show_products(req):

    prod_form = ProductForm()

    if req.method == 'POST':
        print(req.POST)
        # new_product = Product(req.POST[])
        # new_product.save()
        # return HttpResponse(f""" <p>Nuevo producto {new_product.title} creado!</p> """)
    
    products = Product.objects.all()
    return render(req, 'products.html', {'prod_form': prod_form, 'products': products})


def show_employees(req):
    emp_form = EmployeeForm()

    employees = Employee.objects.all()

    return render(req, 'employees.html', {'emp_form': emp_form, 'employees': employees})

def show_suppliers(req):
    supp_form = SupplierForm()

    suppliers = Supplier.objects.all()

    return render(req, 'suppliers.html', {'supp_form': supp_form, 'suppliers': suppliers})