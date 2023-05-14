from pickle import TRUE
from django.db import models
from account.models import User
# Create your models here.
class Room(models.Model):
    creater=models.ForeignKey(User,on_delete=models.CASCADE)
    invited=models.ManyToManyField(User,related_name="invited_user")
    date=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=30)

class Chat(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=2000)
    date=models.DateTimeField(auto_now_add=True)