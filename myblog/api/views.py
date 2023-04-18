from rest_framework import generics

from myblog.blog import models

from . import serializers


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
