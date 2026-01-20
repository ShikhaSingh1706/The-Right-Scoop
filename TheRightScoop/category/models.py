from django.db import models
from core.models import BaseModel


class Category(BaseModel):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    cat_desc=models.TextField(blank=True, null=True)
    cat_img=models.ImageField(upload_to='categories/',blank=True, null=True)
    is_active=models.BooleanField(default=True)
    cat_parent=models.ForeignKey(
        'self',
        on_delete=models.CASCADE, null=True, blank=True,
         related_name='subcategories'
    )

    def __str__(self):
        return self.name

# Create your models here.
