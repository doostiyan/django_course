from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreationForm, UserLoginForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"])

            messages.success(request, message=f"User '{user.username}'created successfully",
                             extra_tags="alert alert-success")

    else:
        form = UserCreationForm()

    return render(request, template_name="users/create.html", context={"form": form})


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                django_login(request, user)
                messages.success(request, message=f"Logged created successfully",
                                 extra_tags="alert alert-success")
                return redirect("books:list")
            else:
                messages.error(request, message="Invalid data.", extra_tags="alert alert-danger")
    else:
        form = UserLoginForm()

    return render(request, template_name="users/login.html", context={"form": form})

# def user_logout(request):
#     logout(request)
#     messages.success(request, message=f"Logged out successfully",
#                      extra_tags="alert alert-success")
#     return redirect("books:list")


class UserLogoutView(LoginRequiredMixin, View):
    # login_url = "/users/login"
    def get(self, request):
        logout(request)

        messages.success(request, message=f"Logged out successfully",
                            extra_tags="alert alert-success")

        return redirect("books:list")