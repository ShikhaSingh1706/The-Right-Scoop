from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display=('id', 'name', 'cat_parent', 'is_active', "created_at", "updated_at")
    list_filter = ('is_active', 'cat_parent')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)

# Register your models here.
