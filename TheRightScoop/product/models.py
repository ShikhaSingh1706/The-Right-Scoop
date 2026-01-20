from django.db import models
from  core.models import BaseModel
from category.models import Category


class Product(BaseModel):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    category=models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )
    price=models.DecimalField(max_digits=10, decimal_places=2)
    product_desc=models.TextField(blank=True)
    quantity=models.PositiveBigIntegerField(default=0)
    is_active=models.BooleanField(default=True)
# Create your models here.


    def __str__(self):
        return self.name

#product image model
class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='product/images/')
    is_primary = models.BooleanField(default=False)
