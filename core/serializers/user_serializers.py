from rest_framework.serializers import ModelSerializer

from core.models import User


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ["id", "is_staff", "is_active", "groups", "user_permissions"]


class DetailUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "created_at", "updated_at"]


class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "id",
            "is_staff",
            "created_at",
            "updated_at",
            "groups",
            "user_permissions",
        ]
