from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration/', views.registration),
    path('add-fighter/', views.add_fighter),
]
