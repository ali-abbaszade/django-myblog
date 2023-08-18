from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from . import forms
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


def signup_view(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email

            if User.objects.filter(username=user.username).exists():
                messages.error(
                    request, f"User with {user.username} email already exists"
                )
                return render(request, "accounts/signup.html", {"form": form})
            else:
                user.save()
                login(request, user)
                messages.success(request, f"Welcome {user.username}")
                return redirect("home")
        else:
            messages.error(request, "An error has occurred.")
            return render(request, "accounts/signup.html", {"form": form})

    else:
        form = forms.SignUpForm()
        return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "username or password is incorrect.")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


class ProfileView(LoginRequiredMixin, DetailView):
    model = models.Profile
    template_name = "accounts/profile.html"

    def get_object(self):
        return models.Profile.objects.get(owner=self.kwargs['id'])