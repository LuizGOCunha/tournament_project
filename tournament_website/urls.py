from django.urls import path, include
from . import views
from .routers import router

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("addfighter/", views.addfighter, name="addfighter"),
    path("api/", include(router.urls)),
]
