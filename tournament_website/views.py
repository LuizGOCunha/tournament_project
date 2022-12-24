import uuid

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

from .models import FighterModel

# Create your views here.

def index(request):
    return render(request, "index.html")

@csrf_protect
def registration(request):
    return render(request, "registration.html")

@csrf_protect
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