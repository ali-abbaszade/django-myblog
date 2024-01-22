from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from myblog.blog import models
from myblog.accounts.models import Profile
from . import serializers


class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorViewSet(ReadOnlyModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.AuthorSerializer


class ProfileViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(owner_id=self.request.user.id)

    @action(detail=False, methods=["GET", "PUT"])
    def me(self, request):
        profile = Profile.objects.get(owner_id=self.request.user.id)
        if request.method == "GET":
            serializer = serializers.ProfileSerializer(profile)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = serializers.ProfileSerializer(
                instance=profile, data=request.data
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
