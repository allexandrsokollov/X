from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
    BooleanField,
    CharField,
    UUIDField,
)

from core.models import Task
from core.serializers.feature_serializers import DetailFeatureSerializer
from core.serializers.user_serializers import DetailUserSerializer


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class DetailTaskSerializer(ModelSerializer):
    owner = DetailUserSerializer()
    feature = DetailFeatureSerializer()

    class Meta:
        model = Task
        fields = "__all__"


class UpdateTaskSerializer(ModelSerializer):
    owner = UUIDField(required=False)
    feature = UUIDField(required=False)
    title = CharField(required=False)
    description = CharField(required=False)
    is_completed = BooleanField(required=False)

    class Meta:
        model = Task
        fields = [
            "owner",
            "feature",
            "title",
            "description",
            "is_completed",
        ]
