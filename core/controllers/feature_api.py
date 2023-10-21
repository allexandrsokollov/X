from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.exceptions.repository_exceptions import NotFoundException
from core.models import Feature
from core.repositories.feature_repository import FeatureRepo
from core.serializers.feature_serializers import FeatureSerializer, DetailFeatureSerializer, \
    UpdateCreateFeatureSerializer
from core.services.feature_service import FeatureService


class FeatureGetAllCreateApiView(APIView):
    model_class = Feature
    create_serializer = UpdateCreateFeatureSerializer
    detail_serializer = FeatureSerializer

    feature_service = FeatureService
    repo = FeatureRepo

    @swagger_auto_schema(
        request_body=create_serializer,
        responses={'200': openapi.Response('detail serializer', detail_serializer)}
    )
    def post(self, request):
        model_data = self.create_serializer(data=self.request.data)
        model_data.is_valid(raise_exception=True)

        new_model = self.feature_service().create(**model_data.validated_data)
        return Response(self.detail_serializer(new_model).data)

    @swagger_auto_schema(
        responses={'200': openapi.Response('response description', detail_serializer(many=True))}
    )
    def get(self, request):
        queryset = self.repo(self.model_class).get_all()
        serializer = self.detail_serializer(queryset, many=True)
        return Response(serializer.data)


class FeatureGetDeleteUpdateApiView(APIView):

    model_class = Feature
    detail_serializer = DetailFeatureSerializer
    update_serializer = UpdateCreateFeatureSerializer

    repo = FeatureRepo
    feature_service = FeatureService

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
        updated_model = self.feature_service().update(pk=pk, **data.validated_data)

        return Response(self.update_serializer(updated_model).data)

    def delete(self, request, pk: str = None):
        try:
            repo = self.repo(self.model_class)
            repo.delete(pk)
        except NotFoundException:
            return Response(status=404)
        return Response(status=200)
