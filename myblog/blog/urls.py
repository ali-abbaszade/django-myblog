from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("write/", views.CreatePostView.as_view(), name="write_post"),
    path("update/<slug:slug>/", views.UpdatePostView.as_view(), name="update_post"),
    path("delete/<slug:slug>/", views.DeletePostView.as_view(), name="delete_post"),
    path("search/", views.PostSearchView.as_view(), name="search"),
    path("<slug:slug>/", views.post_single, name="post_single"),
    path("tag/<slug:slug>/", views.TagListView.as_view(), name="post_tag"),
]
