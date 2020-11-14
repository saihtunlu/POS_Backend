from rest_framework import serializers
from .models import Location, LocationProduct


class LocationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"


class LocationProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = LocationProduct
        fields = "__all__"


class ExportLocationProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = LocationProduct
        fields = ['location', 'quantity', 'sold_out']
