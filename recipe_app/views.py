from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,   'index.html')

def user_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Username or password is wrong!") 
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def user_signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup Successfully. Please login now.") 
            return redirect('user_login')
    return render(request, 'signup.html', {'form': form})