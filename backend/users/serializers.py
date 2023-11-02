from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core import exceptions
from users.models import User


class PasswordChangeSerializer(serializers.Serializer):
    new = serializers.CharField()

    def validate_new(self, value):
        try:
            validate_password(password=value, user=self.context["request"].user)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(list(e.messages))
        return value

    def save(self, *args, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new"])
        user.save()
        return user


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        attrs["user"] = User.objects.filter(email=attrs["email"]).first()
        if not attrs["user"]:
            raise serializers.ValidationError("User with given email not found.")
        return attrs

    def save(self, **kwargs):
        user = self.validated_data["user"]
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        return {"uid": uid, "token": token}


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField()

    def validate_password(self, value):
        try:
            validate_password(password=value)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(list(e.messages))
        return value

    def save(self, **kwargs):
        user = kwargs["user"]
        user.set_password(self.validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )

    def validate_email(self, value):
        if not self.instance and User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "There is already a user associated to this email."
            )
        return value

    def create(self, validated_data):
        validated_password = validated_data.get("password")
        user = User.objects.create(**validated_data)
        user.set_password(validated_password)
        user.save()
        return user
