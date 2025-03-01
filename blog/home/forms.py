from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="",max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),help_text="<span class='form-text text-muted'><small>Required. Max 50 Characters</small></span>")
    first_name= forms.CharField(label="",max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),help_text="<span class='form-text text-muted'><small>Required. Max 50 Characters</small></span>")
    last_name = forms.CharField(label="",max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),help_text="<span class='form-text text-muted'><small>Required. Max 50 Characters</small></span>")
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password1 = forms.CharField(label="",min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholher':'Password'}),help_text="<ul class='form-text text-muted small><li>Your password can\'t be too similar to your other personel information. </li><li>Your password must contain at least 8 characters</li><li>Ypur password can\'t be a commonly used password</li><li>Your password can\'t be entirely numeric.</li></ul>")
    password2 = forms.CharField(label="",min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholher':'Password'}),help_text="<ul class='form-text text-muted small><li>Your password can\'t be too similar to your other personel information. </li><li>Your password must contain at least 8 characters</li><li>Ypur password can\'t be a commonly used password</li><li>Your password can\'t be entirely numeric.</li></ul>")
    

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class SearchForm(forms.Form):
    query = forms.CharField(label='Search',max_length=50)
    
