from rest_framework.serializers import ModelSerializer

from rest_framework.serializers import FloatField, ListField, UUIDField, CharField, SerializerMethodField

from core.models import Project
from core.serializers.user_serializers import DetailUserSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class DetailProjectSerializer(ModelSerializer):
    managers = SerializerMethodField()
    participants = SerializerMethodField()

    def get_managers(self, obj):
        return DetailUserSerializer(obj.managers.all(), many=True).data

    def get_participants(self, obj):
        return DetailUserSerializer(obj.participants.all(), many=True).data

    class Meta:
        model = Project
        fields = '__all__'


class CreateProjectSerializer(ModelSerializer):
    progress = FloatField(required=False, min_value=0)
    participants = ListField(child=UUIDField(), required=False, allow_empty=True)
    managers = ListField(child=UUIDField(), required=False, allow_empty=True)

    class Meta:
        model = Project
        exclude = ['id']


class UpdateProjectSerializer(ModelSerializer):
    progress = FloatField(required=False, min_value=0)
    participants = ListField(child=UUIDField(), allow_empty=True, required=False)
    managers = ListField(child=UUIDField(), allow_empty=True, required=False)
    title = CharField(required=False)
    description = CharField(required=False)

    class Meta:
        model = Project
        fields = [
            'title',
            'progress',
            'description',
            'participants',
            'managers',
        ]
