from django.contrib import admin
from .models import Product, ProductImage, Option,  Variation, Tag
models = [Product, ProductImage, Option,
          Variation, Tag]
# Register your models here.
admin.site.register(models)
