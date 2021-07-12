from django import forms
from .models import Images, Comment

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        exclude = ['profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=['images', 'commented_at']
        