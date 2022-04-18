from django.shortcuts import render, get_list_or_404,redirect
from django.contrib.auth.models import User
from django.http  import HttpResponseRedirect,Http404
from . forms import UpdateUserForm, UpdateUserProfileForm, UserRegisterForm,HoodForm,BusinessForm,PostForm
from .models import Neighbourhood,Business,Post,Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib import messages
# Create your views here.
