from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.exceptions.repository_exceptions import NotFoundException
from core.models import User
from core.repositories.abstract_repos import CRUDRepo
from core.serializers.user_serializers import (
    CreateUserSerializer,
    DetailUserSerializer,
    UpdateUserSerializer,
)


class UserGetAllCreateApiView(APIView):
    model_class = User
    create_serializer = CreateUserSerializer
    detail_serializer = DetailUserSerializer

    repo = CRUDRepo

    @swagger_auto_schema(
        request_body=create_serializer,
        responses={"200": openapi.Response("detail serializer", detail_serializer)},
    )
    def post(self, request):
        user_data = self.create_serializer(data=self.request.data)
        user_data.is_valid(raise_exception=True)

        if not user_data.validated_data.get("username"):
            return Response(status=400, data={"message": "Username is None"})
        if not user_data.validated_data.get("password"):
            return Response(status=400, data={"message": "Password is None"})

        if self.model_class.objects.filter(username=user_data.validated_data.get("username")).exists():
            return Response(
                status=400,
                data={
                    "message": f"Username with this {user_data.validated_data.get("username")} username already exists"
                },
            )

        new_user = self.model_class.objects.create_user(**user_data.validated_data)
        return Response(self.detail_serializer(new_user).data)

    @swagger_auto_schema(
        responses={
            "200": openapi.Response(
                "response description", detail_serializer(many=True)
            )
        }
    )
    @permission_classes([IsAdminUser])
    def get(self, request):
        queryset = self.repo(self.model_class).get_all()
        serializer = self.detail_serializer(queryset, many=True)
        return Response(serializer.data)


class UserGetDeleteUpdateApiView(APIView):
    model_class = User
    detail_serializer = DetailUserSerializer
    update_serializer = UpdateUserSerializer

    repo = CRUDRepo

    @swagger_auto_schema(
        responses={"200": openapi.Response("response description", detail_serializer)}
    )
    @permission_classes([IsAuthenticated])
    def get(self, request, pk=None):
        queryset = self.repo(self.model_class)
        request_user = self.request.user

        if request_user.id != pk:
            return Response(status=403)

        user = get_object_or_404(queryset, pk=pk)

        serializer = self.detail_serializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=update_serializer,
        responses={
            "200": openapi.Response("detail user serializer", update_serializer)
        },
    )
    @permission_classes([IsAuthenticated])
    def put(self, request, pk=None):
        request_user = self.request.user

        if request_user.id != pk:
            return Response(status=403)

        repo = self.repo(self.model_class)
        old_user = repo.get(pk)
        data = self.update_serializer(old_user, data=self.request.data)
        data.is_valid(raise_exception=True)

        repo.update(pk=pk, **data.validated_data)

        return Response(data.data)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk: str = None):
        request_user = self.request.user

        if request_user.id != pk:
            return Response(status=403)

        try:
            repo = self.repo(self.model_class)
            repo.delete(pk)
        except NotFoundException:
            return Response(status=404)
        return Response(status=200)
