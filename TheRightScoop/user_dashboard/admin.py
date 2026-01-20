from django.contrib import admin
from .models import Profile, AddressBook, Wishlist


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'phone', 'profile_photo', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'phone')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'product__product_name')



@admin.register(AddressBook)
class AddressBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'phone', 'city', 'state', 'is_shipping', 'created_at', 'updated_at')
    search_fields = ('user__username', 'full_name', 'city', 'state')
    list_filter = ('is_shipping', 'state', 'country')