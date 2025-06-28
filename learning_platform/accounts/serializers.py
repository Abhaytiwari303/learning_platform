from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_student', 'is_instructor']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_student', 'is_instructor']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
