
from rest_framework import serializers
from .models import Product, ProductImage, Tag,   Option, Variation
from vendor.serializers import VendorSerializers
from location.serializers import LocationProductSerializers, ExportLocationProductSerializers
from category.serializers import Category2Serializers


class ProductImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


class TagSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


# class AttributeSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = Attribute
#         fields = '__all__'


class OptionSerializers(serializers.ModelSerializer):
    values = serializers.JSONField()

    class Meta:
        model = Option
        fields = ['values', 'id', 'name',
                  'created_at', 'updated_at', 'product']


class VariationSerializers(serializers.ModelSerializer):
    locations = LocationProductSerializers(many=True, read_only=True)

    class Meta:
        model = Variation
        fields = ['id', 'variation_name', 'locations', 'regular_price', 'sale_price', 'barcode', 'sku',
                  'is_tracking', 'number_of_stock', 'available_stock', 'threshold_stock', 'sold_out']


class ProductSerializers(serializers.ModelSerializer):
    images = ProductImageSerializers(many=True, read_only=True)
    tags = TagSerializers(many=True, read_only=True)
    category = Category2Serializers(many=False, read_only=True)
    options = OptionSerializers(many=True, read_only=True)
    variations = VariationSerializers(many=True, read_only=True)
    vendor = VendorSerializers(many=False, read_only=True)
    locations = LocationProductSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'images', 'weight', 'length', 'width', 'height', 'weight_unit', 'demission_unit', 'status',
                  'has_variant', 'regular_price', 'sale_price', 'cost_per_item', 'barcode', 'sku',
                  'profit', 'margin', 'is_tracking', 'number_of_stock', 'available_stock', 'threshold_stock', 'sold_out', 'vendor',
                  'category',  'variations', 'tags', 'options', 'locations', 'created_at', 'updated_at']


class ExportProductImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['url']


class ExportOptionSerializers(serializers.ModelSerializer):
    values = serializers.JSONField()

    class Meta:
        model = Option
        fields = ['values', 'name']


class ExportVariationSerializers(serializers.ModelSerializer):
    locations = ExportLocationProductSerializers(many=True, read_only=True)

    class Meta:
        model = Variation
        fields = ['variation_name', 'locations', 'regular_price', 'sale_price', 'barcode', 'sku',
                  'is_tracking', 'number_of_stock', 'available_stock', 'threshold_stock', 'sold_out']


class ExportProductSerializers(serializers.ModelSerializer):
    images = ExportProductImageSerializers(many=True, read_only=True)
    options = ExportOptionSerializers(many=True, read_only=True)
    variations = ExportVariationSerializers(many=True, read_only=True)
    locations = ExportLocationProductSerializers(many=True, read_only=True)
    category = Category2Serializers(many=False, read_only=True)
    tags = TagSerializers(many=True, read_only=True)
    vendor = VendorSerializers(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'images', 'weight', 'length', 'width', 'height', 'demission_unit', 'weight_unit', 'status',
                  'has_variant', 'regular_price', 'sale_price', 'cost_per_item', 'barcode', 'sku',
                  'profit', 'margin', 'is_tracking', 'number_of_stock', 'available_stock', 'threshold_stock', 'sold_out', 'vendor',
                  'category',  'variations', 'tags', 'options', 'locations']
