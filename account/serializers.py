from .models import User
from rest_framework import serializers
# from permission.serializers import UserRoleSerializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'first_name',
                  'last_name', 'email', 'avatar', 'username', 'user_role']
