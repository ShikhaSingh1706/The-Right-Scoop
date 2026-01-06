from django.db import models

class BaseModel(models.Model):
    created_at=models.DateTimeField( auto_now_add=True)  # auto timestamp on create
    updated_at = models.DateTimeField(auto_now=True)      # auto timestamp on update
    is_active = models.BooleanField(default=True)         # soft delete flag

    class Meta:
        abstract = True  # This makes it a base model, no table created