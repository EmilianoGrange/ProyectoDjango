import os
from django.conf import settings
from django.db import models

# Create your models here.

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "images")

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.IntegerField()
    thumbnail = models.FilePathField(path=images_path)

class Employee(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField()
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    start_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

class Supplier(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()