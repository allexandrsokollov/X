from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.exceptions.repository_exceptions import NotFoundException
from core.models import User
from core.repositories.abstract_repos import CRUDRepo
from core.serializers.user_serializers import DetailUserSerializer, CreateUserSerializer, UpdateUserSerializer

class UserGetAllCreateApiView(APIView):

    @swagger_auto_schema(
        request_body=CreateUserSerializer,
        responses={'200': openapi.Response('response description', DetailUserSerializer(many=True))}
    )
    def post(self, request):
        user_data = CreateUserSerializer(data=self.request.data)
        user_data.is_valid(raise_exception=True)

        new_user = CRUDRepo(User).create(**user_data.validated_data)
        return Response(DetailUserSerializer(new_user).data)

    @swagger_auto_schema(
        responses={'200': openapi.Response('response description', DetailUserSerializer)}
    )
    def get(self, request):
        queryset = CRUDRepo(User).get_all()
        serializer = DetailUserSerializer(queryset, many=True)
        return Response({'data': serializer.data})



class UserGetUpdateApiView(APIView):

    @swagger_auto_schema(
        responses={'200': openapi.Response('response description', DetailUserSerializer(many=True))}
    )
    def get(self, request, pk=None):
        queryset = CRUDRepo(User)
        user = get_object_or_404(queryset, pk=pk)

        serializer = DetailUserSerializer(user)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=UpdateUserSerializer,
        responses={'200': openapi.Response('detail user serializer', DetailUserSerializer)}
    )
    def put(self, request, pk=None):
        repo = CRUDRepo(User)
        old_user = repo.get(pk)
        data = UpdateUserSerializer(old_user, data=self.request.data)
        data.is_valid(raise_exception=True)

        repo.update(pk=pk, **data.validated_data)

        return Response(data.data)

    def delete(self, request, pk:str = None):
        try:
            repo = CRUDRepo(User)
            repo.delete(pk)
        except NotFoundException:
            return Response(status=404)
        return Response(status=200)





