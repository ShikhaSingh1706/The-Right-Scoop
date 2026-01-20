from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User
from  product.models import Product


class Cart(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_products')
    quantity=models.PositiveBigIntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    is_active=models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'product')
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

# Create your models here.
