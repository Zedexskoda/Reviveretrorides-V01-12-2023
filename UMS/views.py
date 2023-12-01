from django.shortcuts import render
from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from UMS.models import *
# from .forms import LoginForm
# Create your views here.
app_name='UMS'






from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')  # Redirect to the login page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})







from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(f"Email: {email}, Password: {password}")
            user = authenticate(request, email=email, password=password)
            print(f"User: {user}")
            
            if user is not None:
                login(request, user)
                return redirect('app1:dashboardurls')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'ums/login.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('account:login')  # Replace 'home' with the name of your desired homepage URL or view
