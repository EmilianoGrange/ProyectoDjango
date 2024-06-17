from django.urls import path
from ecommerce.views import home_template, show_products, show_employees, show_suppliers, search_product, detailed_product

urlpatterns = [
    path('', home_template, name='home'),
    path('products/', show_products, name='products'),
    path('search-product/', search_product, name='searchProduct'),
    path('detail-product/<id>', detailed_product, name='detailedProduct'),
    path('employees/', show_employees, name='employees'),
    path('suppliers/', show_suppliers, name='suppliers')
]