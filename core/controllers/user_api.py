from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers.user_serializers import DetailUserSerializer, CreateUserSerializer
from core.repositories.user_repository import UserRepo

class UserApiView(APIView):

    @swagger_auto_schema(
        request_body=CreateUserSerializer,
        responses={'200': openapi.Response('response description', DetailUserSerializer(many=True))}
    )
    def post(self, request):
        user_data = CreateUserSerializer(self.request.data)
        user_data.is_valid(raise_exception=True)

        new_user = user_data.save()
        return Response(DetailUserSerializer(new_user).data)

    @swagger_auto_schema(
        responses={'200': openapi.Response('response description', DetailUserSerializer)}
    )
    def get(self, request):
        queryset = UserRepo().get_all()
        serializer = DetailUserSerializer(queryset, many=True)
        return Response({'data': serializer.data})

    @swagger_auto_schema(
        responses={'200': openapi.Response('response description', DetailUserSerializer(many=True))}
    )
    def get(self, request, pk=None):
        queryset = UserRepo().get_all()
        user = get_object_or_404(queryset, pk=pk)

        serializer = DetailUserSerializer(user)
        return Response(serializer.data)



