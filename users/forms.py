from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):  #This class creates the User registration form
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):   #This class creates the User details update form to update a user's email and password
     email = forms.EmailField()
     
     class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm): #This class will allow users to update their profile picture
    class Meta:
        model = Profile
        fields = ['image']

