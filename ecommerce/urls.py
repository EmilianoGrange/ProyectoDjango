from django.urls import path
from django.contrib.auth.views import LogoutView
from ecommerce.views import *

urlpatterns = [
    path('', home_template, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('staff_auth', staff_auth, name='staffAuth'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', edit_profile, name='editProfile'),
    path('products/', show_products, name='products'),
    path('ordered_products/', ordered_products, name='orderedProducts'),
    path('detail_product/<int:id>', detailed_product, name='detailedProduct'),
    path('create_product/', create_product, name='createProduct'),
    path('search_product/', search_product, name='searchProduct'),
    path('update_product/<int:id>', update_product, name='updateProduct'),
    path('products/<int:id>', del_product, name='deleteProduct'),
    path('employees/', show_employees, name='employees'),
    path('detail_employee/<int:id>', detailed_employee, name='detailedEmployee'),
    path('create_employee/', create_employee, name='createEmployee'),
    path('search_employee/', search_employee, name='searchEmployee'),
    path('update_employee/<int:id>', update_employee, name='updateEmployee'),
    path('employees/<int:id>', del_employee, name='deleteEmployee'),
    path('suppliers/', show_suppliers, name='suppliers'),
    path('detail_supplier/<int:id>', detailed_supplier, name='detailedSupplier'),
    path('create_supplier/', create_supplier, name='createSupplier'),
    path('search_supplier/', search_supplier, name='searchSupplier'),
    path('update_supplier/<int:id>', update_supplier, name='updateSupplier'),
    path('suppliers/<int:id>', del_supplier, name='deleteSupplier')
]