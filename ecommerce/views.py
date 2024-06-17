from django.shortcuts import render
from .models import Supplier, Product, Employee
from .forms import SupplierForm, ProductForm, EmployeeForm

# Create your views here.

def home_template(req):
    return render(req, 'home.html', {})

def show_products(req):
        
    if req.method == 'POST':
        prod_form = ProductForm(req.POST)
        if prod_form.is_valid():
            data = prod_form.cleaned_data
            new_product = Product(**data)
            new_product.save()

    prod_form = ProductForm()
    products = Product.objects.all()
    return render(req, 'products.html', {'prod_form': prod_form, 'products': products})

def search_product(req):
    if req.GET.get('product'):
        try:
            product = Product.objects.get(title__icontains = (req.GET.get('product')).capitalize())
            return render(req, 'search_product.html', {'product': product})
        except:
            return render(req, 'search_product.html', {'product': 'No se encontraron coincidencias'})

    return render(req, 'search_product.html', {})

def del_product(req, id):

    if req.method == 'POST':
        product = Product.objects.get(id=id)
        product.delete()

    prod_form = ProductForm()
    products = Product.objects.all()
    return render(req, 'products.html', {'prod_form': prod_form, 'products': products})

def detailed_product(req, id):
    product = Product.objects.get(id=id)

    return render(req, 'detail_product.html', {'product': product})

def show_employees(req):

    if req.method == 'POST':
        emp_form = EmployeeForm(req.POST)
        if emp_form.is_valid():
            data = emp_form.cleaned_data
            new_employee = Employee(**data)
            new_employee.save()

    empl_form = EmployeeForm()
    employees = Employee.objects.all()
    return render(req, 'employees.html', {'empl_form': empl_form, 'employees': employees})

def show_suppliers(req):

    if req.method == 'POST':
        sup_form = SupplierForm(req.POST)
        if sup_form.is_valid():
            data = sup_form.cleaned_data
            new_supplier = Supplier(**data)
            new_supplier.save()

    supp_form = SupplierForm()
    suppliers = Supplier.objects.all()
    return render(req, 'suppliers.html', {'supp_form': supp_form, 'suppliers': suppliers})