from rest_framework import serializers
from .models import Vendor, BankAccountInformation


class BankAccountInformationSerializers(serializers.ModelSerializer):

    class Meta:
        model = BankAccountInformation
        fields = '__all__'


class VendorSerializers(serializers.ModelSerializer):
    banks = BankAccountInformationSerializers(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = '__all__'
