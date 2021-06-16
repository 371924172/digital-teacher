from rest_framework import serializers
from .models import *
import datetime


class UserSerializer(serializers.ModelSerializer):
    # repassword = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def changePassword(self, validated_data, request):
        user = request.user
        user.set_password(validated_data['password'])
        user.save()
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

    def validate(self, attrs):
        request = self.context.get('request')
        attrs['assign_id'] = request.user.id
        attrs['assign_time'] = datetime.datetime.now()
        return attrs
