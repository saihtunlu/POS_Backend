from django.db import models
from django.conf import settings
from vendor.models import Vendor
from category.models import Category2
User = settings.AUTH_USER_MODEL


class TrackableDateModel(models.Model):
    """Abstract model to Track the creation/updated date for a model."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TrackableDateModel):
    name = models.TextField(max_length=2000, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    status = models.TextField(max_length=2000, null=True)
    has_variant = models.BooleanField(default=False)
    is_tracking = models.BooleanField(default=False)
    number_of_stock = models.TextField(max_length=2000, null=True, default="0")
    available_stock = models.TextField(max_length=2000, null=True, default="0")
    threshold_stock = models.TextField(max_length=2000, null=True, default="0")
    sold_out = models.TextField(max_length=2000, null=True, default="0")
    regular_price = models.TextField(max_length=2000, null=True, default="0")
    sale_price = models.TextField(max_length=2000, null=True, default="0")
    cost_per_item = models.TextField(max_length=2000, null=True, default="0")
    profit = models.TextField(max_length=2000, null=True)
    margin = models.TextField(max_length=2000, null=True)
    barcode = models.TextField(max_length=2000, blank=True, null=True)
    sku = models.TextField(max_length=2000, blank=True, null=True)
    tags = models.ManyToManyField('Tag',  blank=True)
    category = models.ForeignKey(Category2, related_name='products',
                                 null=True, blank=True, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products',
                               null=True, blank=True, on_delete=models.CASCADE)
    weight = models.TextField(max_length=2000, blank=True, null=True)
    length = models.TextField(max_length=2000, blank=True, null=True)
    width = models.TextField(max_length=2000, blank=True, null=True)
    height = models.TextField(max_length=2000, blank=True, null=True)
    weight_unit = models.TextField(max_length=2000, blank=True, null=True)
    demission_unit = models.TextField(max_length=2000, blank=True, null=True)

# class Attribute(TrackableDateModel):
#     product = models.ForeignKey(Product, related_name='attributes',
#                                 null=True, blank=True, on_delete=models.CASCADE)
#     label = models.TextField(max_length=2000, null=True)
#     value = models.TextField(max_length=2000, null=True)


class Option(TrackableDateModel):
    product = models.ForeignKey(Product, related_name='options',
                                null=True, blank=True, on_delete=models.CASCADE)
    name = models.TextField(max_length=2000, null=True)
    values = models.JSONField(default=dict)


class Variation(TrackableDateModel):
    product = models.ForeignKey(Product, related_name='variations',
                                null=True, blank=True, on_delete=models.CASCADE)
    variation_name = models.TextField(max_length=2000, null=True)
    regular_price = models.TextField(max_length=2000, null=True, default="0")
    sale_price = models.TextField(max_length=2000, null=True, default="0")
    barcode = models.TextField(max_length=2000, blank=True, null=True)
    sku = models.TextField(max_length=2000, blank=True, null=True)
    is_tracking = models.BooleanField(default=False)
    number_of_stock = models.TextField(max_length=2000, null=True, default="0")
    available_stock = models.TextField(max_length=2000, null=True, default="0")
    threshold_stock = models.TextField(max_length=2000, null=True, default="0")
    sold_out = models.TextField(max_length=2000, null=True, default="0")


class ProductImage(TrackableDateModel):
    image = models.ImageField(
        upload_to='products/', blank=True, null=True)
    url = models.TextField(max_length=2000, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='images',
                                null=True, blank=True, on_delete=models.CASCADE)


class Tag(TrackableDateModel):
    name = models.TextField(max_length=2000, null=True)
