from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile


# Create your views here.
@login_required(login_url="login")
def Homepage(request):
    return render(request, "home.html")


def SignupPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        repassword = request.POST.get("password2")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")

        if not username or not email or not password or not firstName or not lastName:
            messages.error(request, "All fields are required.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect("signup")

        if password != repassword:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstName
        my_user.last_name = lastName
        my_user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")
    return render(request, "signup.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "Username or Password is incorrect!!!"
            return render(request, "login.html", {"error": error})
    return render(request, "login.html")


def LougoutPage(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def AboutPage(request):
    return render(request, "about.html")


@login_required(login_url="login")
def MyProfile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = None
    context = {"user": user, "profile": profile}
    return render(request, "myprofile.html", context)
