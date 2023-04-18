from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from myblog.blog import models


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    tags = TagListSerializerField()

    class Meta:
        model = models.Post
        fields = ["title", "body", "slug", "author", "tags", "created_at"]
