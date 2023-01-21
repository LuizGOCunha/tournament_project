import uuid

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import FighterModel
from .forms import UserCreationForm

# Create your views here.

def index(request):
    context={}
    return render(request, "index.html", context)

def registration(request):
    context = {}
    context['form'] = UserCreationForm
    if request.method == 'POST':
        password = request.POST['password']
        password_conf = request.POST['password_conf']
        if password == password_conf:
            user = User.objects.create_user(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                username=request.POST['username'],
                email=request.POST['email']
            )
            # Message isnt being sent, have to figure out why
            context['message'] = "User Created Successfully!"
            return redirect("/", context=context)
        else:
            context['message'] = "Password Confirmation Failed. Passwords do no match."

    return render(request, "registration.html", context)

def add_fighter(request):
    if request.method == "POST":
        name = request.POST.get('name')
        weight = request.POST.get('name')
        belt = request.POST.get('name')
        age = request.POST.get('name')
        uid = uuid.uuid4()

        fighter = FighterModel(name=name, weight=weight, belt=belt, age=age, uid=uid)
        fighter.save()

        return JsonResponse({"status":"success"})