from django.contrib import admin
from .models import *
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display=("creater","invited_user","name","date")

    def invited_user(self,obj):
        return "\n".join([user.username for user in obj.invited.all()])

class ChatAdmin(admin.ModelAdmin):
        list_display=("room","user","text","date")

admin.site.register(Chat)

admin.site.register(Room)