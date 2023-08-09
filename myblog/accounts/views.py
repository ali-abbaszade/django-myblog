from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from . import forms


def signup_view(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = forms.SignUpForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)
