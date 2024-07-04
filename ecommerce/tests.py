from django.test import TestCase
from django.urls import reverse
from .models import Product

# Create your tests here.
class DeleteProduct(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            title='Mango',
            description='Fruta Mangifera indica',
            category="Frutas",
            price="1800",
            stock=100)
        self.url = reverse('deleteProduct', args=[self.product.id])

    def test_delete_product(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
        self.assertQuerySetEqual(Product.objects.all(), [])