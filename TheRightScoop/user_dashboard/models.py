from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel
from product.models import Product
# from product.models import Product  # Import your Product model


# Create your models here.
class Profile(BaseModel):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone=models.CharField(max_length=10,blank=True, null=True)
    profile_photo=models.ImageField(upload_to='user_dashboard/profile_photos/',blank=True, null=True)


    def __str__(self):
        return f"{self.user.username}'s profile"
    

# #create wishlist model here
class Wishlist(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted_by')
    
    class Meta:
        unique_together = ('user', 'product')
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"

    def __str__(self):
        return f"{self.product.name}-{self.user.username}"


#address book
class AddressBook(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    full_name=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    email=models.EmailField(blank=True, null=True)
    address_line1=models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='India')
    postal_code = models.CharField(max_length=20)
    is_shipping = models.BooleanField(default=False)  # Marks the default shipping address
    
    class Meta:
        verbose_name="Address"
        verbose_name_plural="Addresses"

    def save(self, *args, **kwargs):
        if self.is_shipping:
            AddressBook.objects.filter(
                user=self.user,
                is_shipping=True
            ).update(is_shipping=False)
        super().save(*args, **kwargs)    

    def __str__(self):
        return f"{self.full_name}-{self.city}-{self.state}"    
       