from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('addfighter/', views.addfighter, name='addfighter'),
]
