from django.contrib import admin
from .models import Profile 
from .models import AddressBook


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'phone', 'profile_photo', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'phone')


@admin.register(AddressBook)
class AddressBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'phone', 'city', 'state', 'is_shipping', 'created_at', 'updated_at')
    search_fields = ('user__username', 'full_name', 'city', 'state')
    list_filter = ('is_shipping', 'state', 'country')