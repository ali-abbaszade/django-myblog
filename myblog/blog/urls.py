from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("write/", views.CreatePostView.as_view(), name="write_post"),
    path("search/", views.PostSearchView.as_view(), name="search"),
    path("<slug:slug>/", views.PostSingleView.as_view(), name="post_single"),
    path("tag/<slug:slug>/", views.TagListView.as_view(), name="post_tag"),
]
