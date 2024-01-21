from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from myblog.blog import models

from . import serializers


class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorCreateList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.AuthorSerializer
