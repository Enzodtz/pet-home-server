from rest_framework import routers, serializers, viewsets, mixins
from core.models import User
from core.serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework.response import Response


class UserViewSet(
    viewsets.ModelViewSet,
    # mixins.CreateModelMixin,
    # mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    # mixins.ListModelMixin,
    # viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["post", "options"]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        try:
            headers = {"Location": str(request.data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            headers = {}

        token_serializer = CustomTokenObtainPairSerializer(data=request.data)
        token_serializer.is_valid(raise_exception=True)

        return Response(
            token_serializer.validated_data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
