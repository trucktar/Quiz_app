from django.contrib.auth import authenticate
from rest_framework import serializers
from django.core.validators import EmailValidator
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']
        read_only_fields = ['username', 'token']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'email': {
                'validators': [EmailValidator]
            }
        }

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.')
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
