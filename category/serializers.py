from rest_framework import serializers
from .models import Category1, Category2


class Category2Serializers(serializers.ModelSerializer):

    class Meta:
        model = Category2
        fields = ['id', 'label']


class Category1Serializers(serializers.ModelSerializer):
    children = Category2Serializers(many=True, read_only=True)

    class Meta:
        model = Category1
        fields = ['id', 'label', 'children']
