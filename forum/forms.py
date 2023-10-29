from django import forms
from forum.models import Thread, Post

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ["forum", "name", "buku"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["body"]