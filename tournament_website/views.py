import uuid

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.db import IntegrityError

from .models import FighterDjangoModel
from .forms import UserCreationForm, SignInForm

# Create your views here.

def index(request:HttpRequest):
    context={}
    if request.user.is_authenticated:
        context['authenticated'] = request.user
    return render(request, "index.html", context)

def registration(request:HttpRequest):
    context = {}
    context['form'] = UserCreationForm
    if request.method == 'POST':
        password = request.POST['password']
        password_conf = request.POST['password_conf']
        if password == password_conf:
            try:
                User.objects.create_user(
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    username = request.POST['username'],
                    email = request.POST['email'],
                    password = request.POST['password']
                )
                # Message isnt showing up, because i'm not able to send the context to rendering
                context['message'] = "User Created Successfully!"
                # If i use render instead of redirect, i'm able to get access to the message
                # However, its not ideal solution because it doesnt change url, only the template
                # Have to find better solution in the future
                return redirect("/signin/")
            except IntegrityError:
                context['message'] = "User Already exists"
        else:
            context['message'] = "Password Confirmation Failed: Passwords do no match."

    return render(request, "registration.html", context)

def signin(request:HttpRequest):
    context = {}
    context['form'] = SignInForm
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['authenticated'] = request.user
            return redirect('/')
        else:
            context['message'] = "Invalid Credentials. Please try again."
    return render(request, "signin.html", context)

def signout(request:HttpRequest):
    logout(request)
    return redirect("/")

def add_fighter(request:HttpRequest):
    pass
    if request.method == "POST":
        name = request.POST['name']
        weight = request.POST['weight']
        belt = request.POST['belt']
        age = request.POST['age']
        uid = uuid.uuid4()

        fighter = FighterDjangoModel(name=name, weight=weight, belt=belt, age=age, uid=uid)
        fighter.save()

        return JsonResponse({"status":"success"})