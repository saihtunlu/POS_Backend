from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class TrackableDateModel(models.Model):
    """Abstract model to Track the creation/updated date for a model."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Vendor(TrackableDateModel):
    name = models.TextField(max_length=2000, null=True)
    address = models.TextField(max_length=2000, blank=True, null=True)
    telephone = models.TextField(max_length=2000, blank=True, null=True)
    website = models.TextField(max_length=2000, blank=True, null=True)
    facebook_page = models.TextField(max_length=2000, blank=True, null=True)
    contact_person = models.TextField(max_length=2000, blank=True, null=True)
    cp_mobile = models.TextField(max_length=2000, blank=True, null=True)
    cp_mail = models.TextField(max_length=2000, blank=True, null=True)

    def __unicode__(self):
        return self.name


class BankAccountInformation(TrackableDateModel):
    vendor = models.ForeignKey(Vendor, related_name='banks',
                               null=True, blank=True, on_delete=models.CASCADE)
    name = models.TextField(max_length=2000, null=True)
    account_number = models.TextField(max_length=2000, null=True)
    account_holder_name = models.TextField(max_length=2000, null=True)
