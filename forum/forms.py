from django import forms
from forum.models import Thread, Post

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
<<<<<<< HEAD
        fields = ["name", "buku"]
=======
        fields = ["forum", "name", "buku"]
>>>>>>> 6dcd09b358ebc9dcac7c707686172bb9d0686c4c

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["body"]