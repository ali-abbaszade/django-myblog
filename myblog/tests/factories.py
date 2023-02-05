import factory
from django.contrib.auth.models import User

from myblog.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test"
    password = "test"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "x"
    body = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    status = "published"
