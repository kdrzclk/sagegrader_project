from rest_framework import serializers
from .models import Institution, User
from django.contrib.auth.password_validation import validate_password

class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution

        fields = (
            "id",
            "inst_name",
            "inst_city",
            "inst_state_code",
            "inst_country",
        )

class UserSerializer(serializers.ModelSerializer):
    institutions = InstitutionSerializer(read_only=True, required=False)
    institutions_id = serializers.CharField(write_only=True, required=False)

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={
            'input_type': 'password'
        }
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={
            'input_type': 'password'
        }
    )

    class Meta:
        model = User
        fields = (
            "id",
            "institutions",
            "institutions_id",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2",
            "user_role",
            "is_active",
            # "is_staff"

        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': "Password field didn't match!"}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    institutions = InstitutionSerializer(read_only=True, required=False)
    institutions_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "institutions",
            "institutions_id",
            "email",
            "first_name",
            "last_name",
            "user_role",
            "is_active",
            # "is_staff"

        )