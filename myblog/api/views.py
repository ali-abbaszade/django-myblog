from rest_framework import generics

from myblog.blog import models

from . import serializers


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class AuthorCreateList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.AuthorSerializer
