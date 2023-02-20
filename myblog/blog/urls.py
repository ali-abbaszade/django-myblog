from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<slug:slug>/", views.PostSingleView.as_view(), name="post_single"),
    path("tag/<slug:slug>/", views.TagListView.as_view(), name="post_tag"),
]
