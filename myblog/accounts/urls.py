from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/<int:id>/", views.ProfileView.as_view(), name="profile"),
    path("profile/update/<int:id>/", views.UpdateProfileView.as_view(), name="update_profile"),
]
