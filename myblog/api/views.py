from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from myblog.blog import models

from . import serializers


class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorViewSet(ReadOnlyModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.AuthorSerializer
