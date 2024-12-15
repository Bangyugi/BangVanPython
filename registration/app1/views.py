from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
        if password == repassword:
            my_user = User.objects.create_user(username, email, password)
            my_user.first_name = firstName
            my_user.last_name = lastName
            my_user.save()
            return redirect("login")
        else:
            return HttpResponse("Fail to create user!")

        print(username, email, password, repassword)

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
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, "login.html")


def LougoutPage(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def AboutPage(request):
    return render(request, "about.html")
