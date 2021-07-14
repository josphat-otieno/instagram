from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.db.models import fields
from django.db.models.base import Model
from .models import Images, Comment, Profile
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        exclude = ['profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=['images', 'commented_at','name']
        

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    
    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        

class UserUpdateForm(forms.ModelForm):
    pass

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        # bio = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": 'form-control'}))
        # profile_photo = forms.ImageField(widget=forms.FileInput)
        #last_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
        fields = ['bio']