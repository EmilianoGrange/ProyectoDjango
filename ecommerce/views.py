from django.shortcuts import render
from .models import Supplier, Product, Employee
from .forms import SupplierForm, ProductForm, EmployeeForm

# Create your views here.

def home_template(req):
    return render(req, 'home.html', {})

def show_products(req):

    products = Product.objects.all()
    return render(req, 'products.html', {'products': products})

def ordered_products(req):
    products = Product.objects.order_by('price')
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

def update_product(req, id):
    if req.method == 'POST':
        prod_form = ProductForm(req.POST)
        if prod_form.is_valid():
            data = prod_form.cleaned_data
            product = Product.objects.get(id=id)
            product.title = data['title']
            product.description = data['description']
            product.category = data['category']
            product.price = data['price']
            product.stock = data['stock']
            product.save()

            return render(req, 'create_product.html', {'message': 'Producto actualizado correctamente'})
    
    product = Product.objects.get(id=id)
    prod_form = ProductForm(initial= {
        'title': product.title,
        'description': product.description,
        'category': product.category,
        'price': product.price,
        'stock': product.stock
    })
    return render(req, 'update_product.html', {'prod_form': prod_form, 'product': product})

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

def update_employee(req, id):
    if req.method == 'POST':
        emp_form = EmployeeForm(req.POST)
        if emp_form.is_valid():
            data = emp_form.cleaned_data
            employee = Employee.objects.get(id=id)
            employee.name = data['name']
            employee.last_name = data['last_name']
            employee.birthday = data['birthday']
            employee.position = data['position']
            employee.salary = data['salary']
            employee.start_date = data['start_date']
            employee.phone_number = data['phone_number']
            employee.email = data['email']
            employee.save()

            return render(req, 'update_employee.html', {'message': 'Colaborador actualizado correctamente'})
    
    employee = Employee.objects.get(id=id)
    emp_form = EmployeeForm(initial= {
            'name': employee.name,
            'last_name': employee.last_name,
            'birthday': employee.birthday,
            'position': employee.position,
            'salary': employee.salary,
            'start_date': employee.start_date,
            'phone_number': employee.phone_number,
            'email': employee.email
    })
    return render(req, 'update_employee.html', {'emp_form': emp_form, 'employee': employee})

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

def update_supplier(req, id):
    if req.method == 'POST':
        supp_form = SupplierForm(req.POST)
        if supp_form.is_valid():
            data = supp_form.cleaned_data
            supplier = Supplier.objects.get(id=id)
            supplier.name = data['name']
            supplier.last_name = data['last_name']
            supplier.phone_number = data['phone_number']
            supplier.email = data['email']
            supplier.save()

            return render(req, 'update_supplier.html', {'message': 'Proveedor actualizado correctamente'})
    
    supplier = Supplier.objects.get(id=id)

    supp_form = SupplierForm(initial= {
        'name': supplier.name,
        'last_name': supplier.last_name,
        'phone_number': supplier.phone_number,
        'email': supplier.email
    })

    return render(req, 'update_supplier.html', {'supp_form': supp_form, 'supplier': supplier})

def del_supplier(req, id):

    if req.method == 'POST':
        supplier = Supplier.objects.get(id=id)
        supplier.delete()

        suppliers = Supplier.objects.all()
        return render(req, 'suppliers.html', {'suppliers': suppliers, 'supplier': supplier})