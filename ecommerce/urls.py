from django.urls import path
from ecommerce.views import home_template, show_products, show_employees, show_suppliers

urlpatterns = [
    path('', home_template, name='home'),
    path('products/', show_products, name='products'),
    path('employees/', show_employees, name='employees'),
    path('suppliers/', show_suppliers, name='suppliers'),
]