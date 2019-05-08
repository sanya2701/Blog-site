from django import forms
from django.forms import ModelForm
from .models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('title','descrip',)

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('author','desc',)
