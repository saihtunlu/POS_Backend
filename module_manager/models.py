from django.db import models


class Modules(models.Model):
    name = models.TextField(max_length=2000, null=True)
    isActivated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
