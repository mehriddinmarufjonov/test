from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import HeaderSerializers
from rest_framework import viewsets
from rest_framework.response import Response

class HeaderViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = HeaderSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        serializer = HeaderSerializers()
        return Response(serializer.data)

