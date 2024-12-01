from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .models import CustomUser
from account.forms import LoginUserForm, NewUserForm, UserPasswordChangeForm, ProfileEditForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Giriş başarılı")
                nextUrl = request.GET.get("next", None)
                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else:
                return render(request,"account/login.html", {"form":form})
        else:
            return render(request,"account/login.html", {"form":form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form":form})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            return render(request, "account/register.html",{"form":form})
    else:
        form = NewUserForm()
        return render(request, "account/register.html",{"form":form})

def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("change_password")
        else:
            return render(request, "account/change-password.html", {"form":form})
    form = UserPasswordChangeForm(request.user)
    return render(request, "account/change-password.html", {"form":form})


def logout_request(request):
    messages.add_message(request, messages.SUCCESS, "Çıkış başarılı")
    logout(request)
    return redirect("index")

@login_required()
def show_profile(request):
    return render(request, "account/show-profile.html", {"user": request.user})

@login_required()
def show_participant(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    
    return render(request, "account/show-participant.html", {"user": user})

@login_required()
def edit_profile(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=user)
        form.save()
        return redirect("show_profile")
    else:
        form = ProfileEditForm(instance=user)
    
    return render(request,"account/edit-profile.html",{"form":form})