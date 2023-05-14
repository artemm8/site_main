import json
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken,RefreshJSONWebToken

# Create your views here.
def register(request):
    if request.method=="POST":
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
        
            return render(request,"registration/register_done.html",{"new_user":new_user})
    else :
        user_form=UserRegistrationForm()
    return render(request,"registration/register.html",{"user_form":user_form})
        
class ObtainJSONWebTokenByEmail(ObtainJSONWebToken):#получаем токены по почте и пароле
    def post(self,request,*args,**kwargs):
        if "email" in request.data:
            try:
                user=User.objects.get(email=request.data["email"])#ищем пользавателя по почте
            except User.DoesNotExist:
                user=None
        if user:
            del request.data["email"]
            request.data["username"]=user.username
        return super().post(request,*args,**kwargs)
class RefreshJSONTokenWith201(RefreshJSONWebToken):#обновление токена
    def post(self,request,*args,**kwargs):
        response=super().post(request,*args,**kwargs)
        if response.status_code==400:
            return Response({"status":"nok"}) 
        return response 

#класс работает по сылкам
obtain_jwt_token=ObtainJSONWebTokenByEmail.as_view()
refresh_jwt_token=RefreshJSONTokenWith201.as_view()