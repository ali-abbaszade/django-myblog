from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from . import forms


def signup_view(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email

            if User.objects.filter(username=user.username).exists():
                messages.error(
                    request, f"User with {user.username} email already exists."
                )
                return render(request, "accounts/signup.html", {"form": form})
            else:
                user.save()
                login(request, user)
                messages.success(request, f"Welcome {user.username}.")
                return redirect("home")
        else:
            messages.error(request, "An error has occurred.")
            return render(request, "accounts/signup.html", {"form": form})

    else:
        form = forms.SignUpForm()
        return render(request, "accounts/signup.html", {"form": form})
