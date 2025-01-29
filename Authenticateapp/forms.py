from django import forms
from django.contrib.auth.models import User
from Authenticateapp.models import UserProfile
from django_recaptcha.fields import ReCaptchaField


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        # fields='__all__'
        fields=['username','password','email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['address','street','city','zipcode','user_img']  
    captcha = ReCaptchaField()              

class Updateform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['address','street','city','zipcode','user_img']             
