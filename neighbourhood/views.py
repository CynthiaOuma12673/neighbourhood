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

def index(request):
    return render(request,'all-neigh/home.html')

def register(request):
    if request.user.is_authenticated:
    #redirect user to the profile page
        return redirect('home')
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request,"registration/register.html",{'form':form})

@login_required(login_url='login')
def hood(request):
    current_user=request.user
    hood = Neighbourhood.objects.all()
    return render(request,"all-neigh/hood.html",{'hood':hood,'current_user':current_user})