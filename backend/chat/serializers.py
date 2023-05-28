from rest_framework import serializers
# from django .contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Room,Chat

User=get_user_model()

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username"]
class RoomSerializer(serializers.ModelSerializer):
    creater=UserSerializers()
    invited=UserSerializers(many=True)
    class Meta:
        model=Room
        fields=("id","creater","invited","name","date")

class ChatSerializers(serializers.ModelSerializer):
    user=UserSerializers ()

    class Meta:
        model=Chat
        fields=["user","text","date"]

class ChatPostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields=["room","text"]