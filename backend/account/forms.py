

from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label="pasword",widget=forms.PasswordInput)
    password2=forms.CharField(label="passwordrepeat",widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=("email",)

    def clean_password2(self):
        cn=self.cleaned_data #получаем данные с полей
        if cn["password"]!=cn["password2"]:
            raise forms.ValidationError("пароли не совпадают")
        return cn["password2"]