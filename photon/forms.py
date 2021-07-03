from django import forms
from django.contrib.auth import models
from . models import Photo,Profile,abc
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UploadPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
    

class ProfileUpload(forms.ModelForm):
    # class Meta:
    #     model = Profile
    #     fields = '__all__'
    class Meta:
        model = Profile
        fields = '__all__'



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField( max_length=50)
    last_name  = forms.CharField( max_length=50)
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']


class Formtest(forms.ModelForm):
    
    class Meta:
        model = abc
        fields = '__all__'
