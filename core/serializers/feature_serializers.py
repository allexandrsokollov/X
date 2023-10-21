from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
    SerializerMethodField,
    CharField,
    UUIDField,
    ListField,
)

from core.models import Feature
from core.serializers.project_serializers import (
    DetailProjectSerializer,
    ProjectSerializer,
)
from core.serializers.user_serializers import DetailUserSerializer


class FeatureSerializer(ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class DetailFeatureSerializer(ModelSerializer):
    executors = SerializerMethodField()
    project = SerializerMethodField()

    def get_project(self, obj):
        if obj.project:
            return ProjectSerializer(obj.project).data

        return

    def get_executors(self, obj):
        return DetailUserSerializer(obj.executors.all(), many=True).data

    class Meta:
        model = Feature
        fields = "__all__"


class UpdateCreateFeatureSerializer(ModelSerializer):
    title = CharField(required=False)
    description = CharField(required=False)
    project = UUIDField(required=False)
    executors = ListField(child=UUIDField(), allow_empty=True, required=False)

    class Meta:
        model = Feature
        fields = [
            "title",
            "description",
            "project",
            "executors",
        ]
