from django.contrib.auth.hashers import make_password
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
        fields = ["id", "username", "email", "password", "posts"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user = models.User.objects.create(
            username=validated_data["username"].lower(),
            password=make_password(validated_data["password"]),
            email=validated_data["email"],
        )
        return user
