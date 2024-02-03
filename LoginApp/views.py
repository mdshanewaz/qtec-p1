from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from LoginApp.models import UserprofileModel
from LoginApp.forms import CreateUserForm, EditProfile

#Pass formate 1234@username

# Create your views here.

def signup_view(request):
    form = CreateUserForm()
    registered = False

    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserprofileModel(user=user)
            user_profile.save()
            
            return HttpResponseRedirect(reverse('LoginApp:login'))

    return render(request, 'LoginApp/signup.html', context={'title':'Signup', 'form':form, 'registered':registered})

def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is  not None:
                login(request, user)
                return HttpResponseRedirect(reverse('ProductApp:home'))

    return render(request, 'LoginApp/login.html', context={'title':'Login', 'form':form})

@login_required
def editprofile_view(request):
    current_user = get_object_or_404(UserprofileModel, user=request.user)
    form = EditProfile(instance=current_user)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('LoginApp:profile'))

    return render(request, 'LoginApp/profile.html', context={'title':'Profile', 'form':form})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('ProductApp:home'))