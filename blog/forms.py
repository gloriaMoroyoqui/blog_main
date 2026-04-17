from django import forms

from .models import Comment 

class CommentForm(forms.Modelform):
    class Meta:
        model = Comment 
        fields = ['name','email','body']