from django.urls import path
from ecommerce.views import *

urlpatterns = [
    path('', home_template, name='home'),
    path('products/', show_products, name='products'),
    path('detail_product/<int:id>', detailed_product, name='detailedProduct'),
    path('create_product/', create_product, name='createProduct'),
    path('search_product/', search_product, name='searchProduct'),
    path('products/<int:id>', del_product, name='deleteProduct'),
    path('employees/', show_employees, name='employees'),
    path('detail_employee/<int:id>', detailed_employee, name='detailedEmployee'),
    path('create_employee/', create_employee, name='createEmployee'),
    path('employees/<int:id>', del_employee, name='deleteEmployee'),
    path('suppliers/', show_suppliers, name='suppliers'),
    path('detail_supplier/<int:id>', detailed_supplier, name='detailedSupplier'),
    path('create_supplier/', create_supplier, name='createSupplier'),
    path('suppliers/<int:id>', del_supplier, name='deleteSupplier')
]