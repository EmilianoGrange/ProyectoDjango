from django.shortcuts import render
from .models import Supplier, Product, Employee
from .forms import SupplierForm, ProductForm, EmployeeForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def home_template(req):
    return render(req, 'home.html', {})

def show_products(req):
    products = Product.objects.all()
    return render(req, 'products.html', {'products': products})

def ordered_products(req):
    products = Product.objects.order_by('price')
    return render(req, 'products.html', {'products': products})

@login_required
def detailed_product(req, id):
    product = Product.objects.get(id=id)
    return render(req, 'detail_product.html', {'product': product})

@staff_member_required(login_url='/ecommerce/staff_auth')
def create_product(req):
    if req.method == 'POST':
        prod_form = ProductForm(req.POST, req.FILES)
        if prod_form.is_valid():
            data = prod_form.cleaned_data
            new_product = Product(**data)
            new_product.save()
            return render(req, 'create_product.html', {'message': 'Producto creado con exito'})
        else:
            return render(req, 'create_product.html', {'message': 'Datos invalidos'})

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

@staff_member_required(login_url='/ecommerce/staff_auth')
def update_product(req, id):
    if req.method == 'POST':
        prod_form = ProductForm(req.POST, req.FILES)
        if prod_form.is_valid():
            data = prod_form.cleaned_data
            product = Product.objects.get(id=id)
            product.title = data['title']
            product.description = data['description']
            product.category = data['category']
            product.price = data['price']
            product.stock = data['stock']
            product.thumbnail = data['thumbnail']
            product.save()
            return render(req, 'update_product.html', {'message': 'Producto actualizado correctamente'})
        else:
            return render(req, 'update_product.html', {'message': 'Datos invalidos'})

    product = Product.objects.get(id=id)
    prod_form = ProductForm(initial= {
        'title': product.title,
        'description': product.description,
        'category': product.category,
        'price': product.price,
        'stock': product.stock,
        'thumbnail': product.thumbnail
    })
    return render(req, 'update_product.html', {'prod_form': prod_form, 'product': product})

@staff_member_required(login_url='/ecommerce/staff_auth')
def del_product(req, id):
    if req.method == 'POST':
        product = Product.objects.get(id=id)
        product.delete()
        products = Product.objects.all()
        return render(req, 'products.html', {'products': products, 'product': product})

@login_required
def show_employees(req):
    employees = Employee.objects.all()
    return render(req, 'employees.html', {'employees': employees})

@staff_member_required(login_url='/ecommerce/staff_auth')
def detailed_employee(req, id):
    employee = Employee.objects.get(id=id)
    return render(req, 'detail_employee.html', {'employee': employee})

@staff_member_required(login_url='/ecommerce/staff_auth')
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

@login_required
def search_employee(req):
    if req.GET.get('employee'):
        try:
            employee = Employee.objects.get(last_name__icontains = (req.GET.get('employee')).capitalize())
            return render(req, 'search_employee.html', {'employee': employee})
        except:
            return render(req, 'search_employee.html', {'employee': 'No se encontraron coincidencias'})

    return render(req, 'search_employee.html', {})

@staff_member_required(login_url='/ecommerce/staff_auth')
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

@staff_member_required(login_url='/ecommerce/staff_auth')
def del_employee(req, id):
    if req.method == 'POST':
        employee = Employee.objects.get(id=id)
        employee.delete()
        employees = Employee.objects.all()
        return render(req, 'employees.html', {'employees': employees, 'employee': employee})

@login_required
def show_suppliers(req):
    suppliers = Supplier.objects.all()
    return render(req, 'suppliers.html', {'suppliers': suppliers})

@staff_member_required(login_url='/ecommerce/staff_auth')
def detailed_supplier(req, id):
    supplier = Supplier.objects.get(id=id)
    return render(req, 'detail_supplier.html', {'supplier': supplier})

@staff_member_required(login_url='/ecommerce/staff_auth')
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

@login_required
def search_supplier(req):
    if req.GET.get('supplier'):
        try:
            supplier = Supplier.objects.get(last_name__icontains = (req.GET.get('supplier')).capitalize())
            return render(req, 'search_supplier.html', {'supplier': supplier})
        except:
            return render(req, 'search_supplier.html', {'supplier': 'No se encontraron coincidencias'})

    return render(req, 'search_supplier.html', {})

@staff_member_required(login_url='/ecommerce/staff_auth')
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

@staff_member_required(login_url='/ecommerce/staff_auth')
def del_supplier(req, id):
    if req.method == 'POST':
        supplier = Supplier.objects.get(id=id)
        supplier.delete()
        suppliers = Supplier.objects.all()
        return render(req, 'suppliers.html', {'suppliers': suppliers, 'supplier': supplier})

def register(req):
    if req.method == 'POST':
        reg_form = UserCreationForm(req.POST)
        if reg_form.is_valid():
            data = reg_form.cleaned_data
            user = data['username']
            reg_form.save()
            return render(req, 'register.html', {'message': f'Usuario {user} creado con exito!'})
        else:
            return render(req, 'register.html', {'message': 'Datos invalidos'})

    reg_form = UserCreationForm()
    return render(req, 'register.html', {'reg_form': reg_form})

def login_view(req):
    if req.method == 'POST':
        auth_form = AuthenticationForm(req, data=req.POST)
        if auth_form.is_valid():
            data = auth_form.cleaned_data
            user = data['username']
            password = data['password']
            authenticated = authenticate(username=user, password=password)
            if authenticated:
                login(req, authenticated)
                return render(req, 'login.html', {'message': f'Bienvenido, {user}!'})
            else:
                return render(req, 'login.html', {'message': 'Datos erroneos'})
        else:
            return render(req, 'login.html', {'message': 'Datos invalidos'})

    auth_form = AuthenticationForm()
    return render(req, 'login.html', {'auth_form': auth_form})

def staff_auth(req):
    if req.method == 'POST':
        auth_form = AuthenticationForm(req, data=req.POST)
        if auth_form.is_valid():
            data = auth_form.cleaned_data
            user = data['username']
            password = data['password']
            authenticated = authenticate(username=user, password=password)
            if authenticated:
                login(req, authenticated)
                return render(req, 'staff_auth.html', {'message': f'Bienvenido, {user}!'})
            else:
                return render(req, 'staff_auth.html', {'message': 'Datos erroneos'})
        else:
            return render(req, 'staff_auth.html', {'message': 'Datos invalidos'})

    auth_form = AuthenticationForm()
    return render(req, 'staff_auth.html', {'auth_form': auth_form})

@login_required
def edit_profile(req):
    user = req.user
    if req.method == 'POST':
        profile_form = UserEditForm(req.POST, instance=user)
        if profile_form.is_valid():
            data = profile_form.cleaned_data
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.set_password(data['psw1'])
            user.save()
            return render(req, 'profile.html', {'message': 'Perfil actualizado correctamente'})
        else:
            return render(req, 'profile.html', {'profile_form': profile_form})

    profile_form = UserEditForm(instance=user)
    return render(req, 'profile.html', {'profile_form': profile_form})