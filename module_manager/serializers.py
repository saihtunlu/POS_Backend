from rest_framework import serializers
from .models import Modules


class ModulesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Modules
        fields = ['id',  'name',
                  'isActivated', 'created_at']
