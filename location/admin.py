from django.contrib import admin
from .models import Location, LocationProduct
# Register your models here.
admin.site.register([Location, LocationProduct])
