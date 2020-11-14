from django.db import models
from product.models import Variation, Product


class TrackableDateModel(models.Model):
    """Abstract model to Track the creation/updated date for a model."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Location(TrackableDateModel):
    name = models.TextField(max_length=2000, null=True)


class LocationProduct(TrackableDateModel):
    variation_product = models.ForeignKey(Variation, related_name='locations',
                                          null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='locations',
                                null=True, blank=True, on_delete=models.CASCADE)

    location = models.ForeignKey(Location, related_name='products',
                                 null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.TextField(max_length=2000, null=True, default="0")
    sold_out = models.TextField(max_length=2000, null=True, default="0")
