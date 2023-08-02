import pytest
import json
from myblog.blog import models
from django.contrib.auth.models import User
from django.urls import reverse

pytestmark = pytest.mark.django_db


# Test Get Posts
def test_zero_posts_should_return_empty_list(client):
    response = client.get(reverse("posts"))
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_post_exists_should_succeed(client):
    author = User.objects.create(username="test", password="test")
    test_post = models.Post.objects.create(
        title="Test", body="Test Content", author=author, slug="test-post"
    )
    response = client.get(reverse("posts"))
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content[0].get("title") == test_post.title
    assert response_content[0].get("body") == test_post.body
    assert response_content[0].get("slug") == test_post.slug


# Test Get Author
def test_zero_authors_should_return_empty_list(client):
    author = User.objects.create(username="test", password="test")
    response = client.get(reverse("author_detail", args=[author.id]))
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content.get("username") == author.username


# Test Post Author
def test_create_author_should_pass(client):
    response = client.post(
        reverse("authors"),
        data={"username": "test", "email": "test@email.com", "password": "test"},
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("email") == "test@email.com"


def test_create_author_without_arguments_should_fail(client):
    response = client.post(reverse("authors"))
    response.status_code == 400


def test_existing_author_should_fail(client):
    author = User.objects.create(username="test", password="test")
    response = client.post(
        reverse("authors"),
        data={"username": author.username, "password": author.password},
    )
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "username": ["A user with that username already exists."]
    }
