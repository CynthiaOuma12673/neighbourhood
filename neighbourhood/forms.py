from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import EmailInput
from . models import Neighbourhood,Post,Business,Profile
from django.forms.widgets import Textarea

