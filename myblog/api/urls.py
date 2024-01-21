from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()
router.register("posts", views.PostViewSet)


urlpatterns = [
    path("authors/", views.AuthorCreateList.as_view(), name="authors"),
    path("authors/<int:pk>/", views.AuthorDetail.as_view(), name="author_detail"),
    path("", include(router.urls)),
]
