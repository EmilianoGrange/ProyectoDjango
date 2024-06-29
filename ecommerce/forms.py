from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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
    thumbnail = forms.ImageField()

class EmployeeForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    birthday = forms.DateField()
    position = forms.CharField()
    salary = forms.DecimalField()
    start_date = forms.DateField()
    phone_number = forms.CharField()
    email = forms.EmailField()

class UserEditForm(UserChangeForm):
    password = forms.CharField(widget=forms.HiddenInput(), required=False)

    psw1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    psw2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_psw2(self):
        psw1 = self.cleaned_data['psw1']
        psw2 = self.cleaned_data['psw2']
        if psw1 != psw2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return psw2