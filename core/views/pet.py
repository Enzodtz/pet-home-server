from django.conf import settings
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, viewsets
from core.models import Pet
from core.serializers import PetSerializer
from rest_framework.parsers import MultiPartParser, FileUploadParser


class PetViewPagination(CursorPagination):
    ordering = "-name"


class PetView(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    parser_classes = (MultiPartParser,)
    pagination_class = PetViewPagination
