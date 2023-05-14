from tkinter import dialog
from django import urls
from django.urls import path,include
from .views import *

urlpatterns=[
    path("room/",RoomAPI.as_view()),
    path("dialog/",DialogAPI.as_view()),
    path("users/",AddUserRoomApi.as_view()),
    
]