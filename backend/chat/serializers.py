from rest_framework import serializers
from django .contrib.auth.models import User
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username"]
class RoomSerializer(serializers.ModelSerializer):
    creater=UserSerializers()
    invited=UserSerializers(many=True)
    class Meta:
        model=Room
        fields=("creater","inviter","name","date","id")

class ChatSerializers(serializers.ModelSerializer):
    user=UserSerializers ()

    class Meta:
        model=Chat
        fields=["user","text","date"]

class ChatPostSerializers(serializers.ModelSerializer):
    class Meta:
        models=Chat
        fields=["room","text"]