from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    proname = models.CharField(max_length=20)
    proprice = models.IntegerField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.proname
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    quantity = models.PositiveIntegerField(default=1)  

    def subtotal(self):
        return self.product.proprice * self.quantity
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    quantity = models.PositiveIntegerField(default=1)  

    def subtotal(self):
        return self.product.proprice * self.quantity
