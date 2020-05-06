from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'about', 'content', 'author', 'image', 'source')


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'about', 'content', 'author', 'source')









