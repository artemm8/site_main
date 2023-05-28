
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Room,Chat
from .serializers import RoomSerializer,ChatSerializers,UserSerializers,ChatPostSerializers
from django.contrib.auth.models import User
from django.db.models import Q# это логическоя or'
#первое что нужно сделать взять записи из базы данных 
#2 серилизаровать данные в json
#3 отдаем пользавателю ответ
class RoomAPI(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    #сдесь отдаем комнаты пользавателя
    def get(self,request):
        rooms=Room.objects.filter(Q(creater=request.user)|Q(invited=request.user))
        serializer=RoomSerializer(rooms,many=True)
        return Response(
            {"data":serializer.data}
        )
    def post(self,request):
        Room.objects.create(creater=request.user)
        return Response(status=201)#отдаем ответ все сохранилось

class DialogAPI(APIView):
    permission_classes=[permissions.IsAuthenticated,]
    def get(self,request):
        room=request.GET.get("room")
        chat=Chat.objects.filter(room=room)
        serializer=ChatSerializers(chat,many=True)
        return Response(
        {"data":serializer.data}
            
        )

    def post(self,request):
        dialog=ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else :
            return Response(status=400)

class AddUserRoomApi(APIView):
    def get(self,request):
        users=User.objects.all()
        serializer=UserSerializers(users,many=True)
        return Response(serializer.data)

    def post(self,request):
        room=request.data.get("room")
        user=request.data.get("user")
        try:
            room=Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)