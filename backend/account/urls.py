from django import urls
from django.urls import path,include
from .views import *

urlpatterns=[
    path("",include("django.contrib.auth.urls")),
    path("register/",register,name="register"),
    path("auth/obtain_token/",obtain_jwt_token),




]