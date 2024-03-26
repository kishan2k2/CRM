from django.shortcuts import render, redirect
from .models import * # If it doesn't work out then I will import User directly from django.contrib.authenticate itself.\
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages # What is this message for?
from django.contrib.auth import authenticate, login as auth_login, logout as Logout

# Create your views here.
username = ""
def home(request):
    if username != "":
        return render(request, 'home.html', {
            'username': f'{username}'
        })
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid user')
            redirect('/app/register')
        else:
            user = authenticate(username = username, password = password)
            if user is None:
                messages.error(request, 'Invalid password')
                return redirect('/app/login')
            else:
                auth_login(request, user)
                # redirect('/app/')
                return render(request, 'home.html', {
                    'username': f'{username}'
                })
            

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm = request.POST.get('password2')
        print(password)
        print(confirm)
        if password!=confirm:
            return render(request, 'register.html', {
                "error":"Password didn't match try again"
            })
        user = User.objects.filter(username = username)
        print("Username is ", username)
        if user.exists():
            messages.info(request, "User name already taken") # What does this do I dont understand lets watch.
            print("Username already exist.")
            return redirect('/app/register')
        else:
            user = User.objects.create_user(
                username = username
            )
            user.set_password(password)
            user.save()
            messages.info(request, 'Account created sucessfully')
            print("new account created")
            return redirect('/app/login')
            
        
    return render(request, 'register.html')
@login_required
def logout(request):
    global username
    username = ""
    Logout(request)
    return redirect('/app/')