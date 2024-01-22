from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from myblog.blog import models
from myblog.accounts.models import Profile


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = TagListSerializerField()

    class Meta:
        model = models.Post
        fields = [
            "id",
            "title",
            "body",
            "slug",
            "status",
            "author",
            "tags",
            "created_at",
        ]

    def create(self, validated_data):
        return models.Post.objects.create(
            author_id=self.context["request"].user.id, **validated_data
        )


class AuthorSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name="post-detail", many=True, read_only=True
    )

    class Meta:
        model = models.User
        fields = ["id", "username", "email", "password", "posts"]


class ProfileSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "owner_id", "name", "about"]
