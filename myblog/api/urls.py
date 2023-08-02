from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("posts/", views.PostList.as_view(), name="posts"),
    path("posts/<int:pk>", views.PostDetail.as_view(), name="post_detail"),
    path("authors/", views.AuthorCreateList.as_view(), name="authors"),
    path("authors/<int:pk>", views.AuthorDetail.as_view(), name="author_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
