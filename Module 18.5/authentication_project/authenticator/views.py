from django.shortcuts import render, redirect
from authenticator.forms import RegisterForm, MyPasswordChangeForm, ChangeUserData, MySetPasswordForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if not request.user.is_authenticated:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully')
                return redirect('sign_up')  # Redirect to clear the form and avoid re-posting on refresh

        return render(request, 'sign_up.html', {'form': form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(request= request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password= userpass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')
                    return redirect('profile')
        return render(request, 'login.html', {'form' : form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        form = ChangeUserData(instance = request.user)
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Updated Successfully')
                return redirect('profile')  # Redirect to clear the form and avoid re-posting on refresh

        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('sign_up')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        form = MyPasswordChangeForm(user=request.user)
        if request.method == 'POST':
            form = MyPasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                return redirect('profile')
        return render(request, 'passchange.html', {'form' : form})
    else:
        return redirect('login')

def pass_change2(request):
    if request.user.is_authenticated:
        form = MySetPasswordForm(user=request.user)
        if request.method == 'POST':
            form = MySetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                return redirect('profile')
        return render(request, 'passchange.html', {'form' : form})
    else:
        return redirect('login')
