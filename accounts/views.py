import json
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from django.urls import reverse
from .forms import SignupForm 
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('******')
            user = form.save()
            print(user)
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})

def sign_in(request):
    resp = {"status":'failed'}
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            resp['status'] = 'success'

            
        else:
            resp['status'] = 'failed'
            return HttpResponse(json.dumps(resp), content_type= 'application/json')
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
    return render(request, "accounts/signin.html")

def sign_out(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

def user_profile(request):
    return render(request,'accounts/user_profile.html')


