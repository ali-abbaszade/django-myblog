from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from myblog.blog import models


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    tags = TagListSerializerField()

    class Meta:
        model = models.Post
        fields = ["id", "title", "body", "slug", "author", "tags", "created_at"]


class AuthorSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name="post_detail", many=True, read_only=True
    )

    class Meta:
        model = models.User
        fields = ["id", "username", "posts"]
