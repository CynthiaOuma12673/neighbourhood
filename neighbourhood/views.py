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

@login_required(login_url='login')
def profile(request, username):
    current_user=request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)

    return render(request, 'all-neigh/profile.html', {'user_form':user_form,'profile_form':profile_form})

@login_required(login_url='login')
def new_hood(request):
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user
            hood.save()
            return HttpResponseRedirect(reverse("hood"))
    else:
        form = HoodForm()
    return render(request, 'all-neigh/new_hood.html', {'form': form})

@login_required(login_url='login')
def user(request,id):
    current_user = request.user
    hood = Neighbourhood.objects.get(id=id)
    members = Profile.objects.filter(neighbourhood=hood)
    businesses = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(neighbourhood=hood)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    
    return render(request, 'all-neigh/user.html', {'hood': hood,'businesses':businesses,'posts':posts,'current_user':current_user,'members':members})
    
@login_required(login_url='login')
def leave_hood(request,id):
    hood = Neighbourhood.objects.get(id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')