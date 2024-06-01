from django import forms

class SupplierForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField()

class ProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    category = forms.CharField()
    price = forms.DecimalField()
    stock = forms.IntegerField()

class EmployeeForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    #birthday = forms.DateField()
    position = forms.CharField()
    salary = forms.DecimalField()
    start_date = forms.DateField()
    phone_number = forms.CharField()
    email = forms.EmailField()