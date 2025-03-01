from django import forms
from django.contrib.auth.models import User
from .models import Article,Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title',"content","image"]

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ["text"]
        labels={
            'text':'',
        }
        widgets={
            "text":forms.Textarea(attrs={'rows':5, "cols":80,"placeholder":"Comment"}),
            
        }