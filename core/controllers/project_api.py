from django.db import transaction
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from core.exceptions.repository_exceptions import NotFoundException
from core.models import Project
from core.repositories.project_repository import ProjectRepo
from core.serializers.project_serializers import ProjectSerializer, DetailProjectSerializer, CreateProjectSerializer, \
    UpdateProjectSerializer


class ProjectGetAllCreateApiView(APIView):
    model_class = Project
    create_serializer = CreateProjectSerializer
    detail_serializer = ProjectSerializer

    repo = ProjectRepo

    @swagger_auto_schema(
        request_body=create_serializer,
        responses={'200': openapi.Response('detail serializer', detail_serializer)}
    )
    def post(self, request):
        model_data = self.create_serializer(data=self.request.data)
        model_data.is_valid(raise_exception=True)

        new_model = self.repo(self.model_class).create(**model_data.validated_data)
        return Response(self.detail_serializer(new_model).data)

    @swagger_auto_schema(
        responses={'200': openapi.Response('response description', detail_serializer(many=True))}
    )
    def get(self, request):
        queryset = self.repo(self.model_class).get_all()
        serializer = self.detail_serializer(queryset, many=True)
        return Response(serializer.data)


class ProjectGetDeleteUpdateApiView(APIView):

    model_class = Project
    detail_serializer = DetailProjectSerializer
    update_serializer = UpdateProjectSerializer

    repo = ProjectRepo

    @swagger_auto_schema(
        responses={'200': openapi.Response('response description', detail_serializer)}
    )
    def get(self, request, pk=None):
        queryset = self.repo(self.model_class)
        model = get_object_or_404(queryset, pk=pk)

        serializer = self.detail_serializer(model)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=update_serializer,
        responses={'200': openapi.Response('detail user serializer', update_serializer)}
    )
    @transaction.atomic
    def put(self, request, pk=None):
        repo = self.repo(self.model_class)
        old_model = repo.get(pk)
        data = self.update_serializer(old_model, data=self.request.data)

        data.is_valid(raise_exception=True)
        repo.update(pk=pk, **data.validated_data)
        new_model = repo.get(pk)

        return Response(self.detail_serializer(new_model).data)

    def delete(self, request, pk: str = None):
        try:
            repo = self.repo(self.model_class)
            repo.delete(pk)
        except NotFoundException:
            return Response(status=404)
        return Response(status=200)
