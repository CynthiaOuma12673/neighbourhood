from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import EmailInput
from . models import Neighbourhood,Post,Business,Profile
from django.forms.widgets import Textarea

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields= ['username','email','password1','password2']
        
User._meta.get_field('email')._unique=True

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')