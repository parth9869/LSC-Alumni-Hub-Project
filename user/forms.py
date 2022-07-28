# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from requests import request
from .models import CustomUser
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control rounded-3'}),required=True)
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-3','type':'password'}),required=True)
    
    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')

        

        if not CustomUser.objects.filter(email=email).exists():
                 
            raise forms.ValidationError({'email':"user does not exist"})
        
        elif not CustomUser.objects.get(email=email).check_password(password):
                raise forms.ValidationError({'password':"email and password incorrect."})  
            
    class Meta(UserCreationForm):
        model = CustomUser
        fields=['email','password']

class UserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['username'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['firstname'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['lastname'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['password1'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['password2'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['usertype'].widget.attrs.update({'class':'form-control rounded-3'})
    
    class Meta(UserCreationForm):
        model = CustomUser
       
        fields = ('username','email','firstname','lastname','usertype','password1','password2')

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username','email','firstname','lastname')
