import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


class TestTag:
    def test_tag_url(self, client, post_factory):
        post_factory(title="test-post", tags=["test-tag"])
        url = reverse("post_tag", kwargs={"slug": "test-tag"})
        response = client.get(url)
        assert response.status_code == 200

    def test_post_htmx_fragment(self, client, post_factory):
        post_factory(title="test-post", tags=["test-tag"])
        headers = {"HTTP_HX-Request": "true"}
        url = reverse("post_tag", kwargs={"slug": "test-tag"})
        response = client.get(url, **headers)
        assertTemplateUsed(response, "blog/components/tag-post-list-elements.html")

    def test_tag_filter(self, client, post_factory):
        post = post_factory(title="test-post", tags=["test-tag"])
        url = reverse("post_tag", kwargs={"slug": "test-tag"})
        response = client.get(url)
        assert post.tags.all()[0].name == response.context["slug"]
