from django import urls
from django.urls import path,include
from .views import register,obtain_jwt_token,refresh_jwt_token
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path("",include("django.contrib.auth.urls")),
    path("register/",register,name="register"),
    # path("auth/obtain_token/",obtain_jwt_token),
    # path("auth/refresh_token/",refresh_jwt_token),
    path("token/",obtain_auth_token)



]