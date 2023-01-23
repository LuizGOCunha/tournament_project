from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration/', views.registration, name='registration'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('add-fighter/', views.add_fighter, name='add-fighter'),
]
