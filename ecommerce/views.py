from django.shortcuts import render
from .models import Supplier, Product, Employee
from .forms import SupplierForm, ProductForm, EmployeeForm

# Create your views here.

def home_template(req):
    return render(req, 'home.html', {})

def show_products(req):

    products = Product.objects.all()
    return render(req, 'products.html', {'products': products})

def detailed_product(req, id):
    product = Product.objects.get(id=id)

    return render(req, 'detail_product.html', {'product': product})

def create_product(req):
    if req.method == 'POST':
        prod_form = ProductForm(req.POST)
        if prod_form.is_valid():
            data = prod_form.cleaned_data
            new_product = Product(**data)
            new_product.save()

            return render(req, 'create_product.html', {'message': 'Producto creado con exito'})

    prod_form = ProductForm()
    return render(req, 'create_product.html', {'prod_form': prod_form})

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

        products = Product.objects.all()
        return render(req, 'products.html', {'products': products, 'product': product})

def show_employees(req):

    employees = Employee.objects.all()
    return render(req, 'employees.html', {'employees': employees})

def detailed_employee(req, id):
    employee = Employee.objects.get(id=id)

    return render(req, 'detail_employee.html', {'employee': employee})

def create_employee(req):

    if req.method == 'POST':
        emp_form = EmployeeForm(req.POST)
        if emp_form.is_valid():
            data = emp_form.cleaned_data
            new_employee = Employee(**data)
            new_employee.save()

            return render(req, 'create_employee.html', {'message': 'Empleado creado con exito'})

    empl_form = EmployeeForm()
    return render(req, 'create_employee.html', {'empl_form': empl_form})

def search_employee(req):
    if req.GET.get('employee'):
        try:
            employee = Employee.objects.get(last_name__icontains = (req.GET.get('employee')).capitalize())
            return render(req, 'search_employee.html', {'employee': employee})
        except:
            return render(req, 'search_employee.html', {'employee': 'No se encontraron coincidencias'})

    return render(req, 'search_employee.html', {})

def del_employee(req, id):

    if req.method == 'POST':
        employee = Employee.objects.get(id=id)
        employee.delete()

        employees = Employee.objects.all()
        return render(req, 'employees.html', {'employees': employees, 'employee': employee})

def show_suppliers(req):

    suppliers = Supplier.objects.all()
    return render(req, 'suppliers.html', {'suppliers': suppliers})

def detailed_supplier(req, id):
    supplier = Supplier.objects.get(id=id)

    return render(req, 'detail_supplier.html', {'supplier': supplier})

def create_supplier(req):

    if req.method == 'POST':
        sup_form = SupplierForm(req.POST)
        if sup_form.is_valid():
            data = sup_form.cleaned_data
            new_supplier = Supplier(**data)
            new_supplier.save()

            return render(req, 'create_supplier.html', {'message': 'Proveedor creado con exito'})

    supp_form = SupplierForm()
    return render(req, 'create_supplier.html', {'supp_form': supp_form})

def search_supplier(req):
    if req.GET.get('supplier'):
        try:
            supplier = Supplier.objects.get(last_name__icontains = (req.GET.get('supplier')).capitalize())
            return render(req, 'search_supplier.html', {'supplier': supplier})
        except:
            return render(req, 'search_supplier.html', {'supplier': 'No se encontraron coincidencias'})

    return render(req, 'search_supplier.html', {})

def del_supplier(req, id):

    if req.method == 'POST':
        supplier = Supplier.objects.get(id=id)
        supplier.delete()

        suppliers = Supplier.objects.all()
        return render(req, 'suppliers.html', {'suppliers': suppliers, 'supplier': supplier})