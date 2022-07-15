from wsgiref.validate import validator
from rest_framework import serializers
from core.models import User
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "cellphone",
            "first_name",
            "last_name",
        ]

        extra_kwargs = {
            "id": {
                "read_only": True,
            },
            "email": {
                "validators": [
                    EmailValidator,
                    UniqueValidator(
                        queryset=User.objects.all(), message="Email already registered!"
                    ),
                ],
            },
            "password": {
                "write_only": True,
                "validators": [validate_password],
            },
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
