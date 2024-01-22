from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register("posts", views.PostViewSet)
router.register("authors", views.AuthorViewSet)
router.register("profiles", views.ProfileViewSet, basename="profiles")


urlpatterns = [
    path("", include(router.urls)),
]
