from django.db import models

#def images_path():
#    return os.path.join(settings.LOCAL_FILE_DIR, "images")

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.last_name}, {self.name} - {self.email}'
    
    #class Meta():
    #    verbose_name = 'Proveedor'
    #    verbose_name_plural = 'Proveedores'
    #    ordering = ('last_name', 'email')
    #    unique_together = ('name', 'last_name', 'email')
    
class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.IntegerField()
    thumbnail = models.ImageField(upload_to='products', blank=True, null=True)
    #supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    #supplier = models.ManyToManyField(Supplier)

    def __str__(self):
        return f'{self.title} - {self.category} - ${self.price}'
    
    #class Meta():
    #    verbose_name = 'Producto'
    #    verbose_name_plural = 'Mercaderia'
    #    ordering = ('title', 'price')
    #    unique_together = ('title', 'description', 'category')

class Employee(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField()
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    start_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.last_name}, {self.name} - {self.position}'
    
    #class Meta():
    #    verbose_name = 'Empleado'
    #    verbose_name_plural = 'Colaboradores'
    #    ordering = ('last_name',)
    #    unique_together = ('name', 'last_name', 'email')