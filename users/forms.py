from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm



class RegisterFormUser(UserCreationForm):
    email = forms.EmailField()
    # first_name = forms.CharField( max_length=20)
    # last_name = forms.CharField( max_length=20)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email')


class ProfilePicUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']