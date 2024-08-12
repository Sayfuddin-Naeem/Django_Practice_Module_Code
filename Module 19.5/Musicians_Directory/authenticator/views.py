from django.shortcuts import render, redirect
from authenticator.forms import RegisterForm, MyPasswordChangeForm, ChangeUserDataForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from musicians_directory_app.models import AlbumModel
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView, ListView
    
class SignupFormView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'sign_up.html'
    success_url = 'signup'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Account Information Incorrect')
        return super().form_invalid(form)
    

class UserLoginView(LoginView):
    template_name = 'login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Logged in information incorrect')
        return response

@method_decorator(login_required, name='dispatch')
class ProfileView(ListView):
    model = AlbumModel
    template_name = 'profile.html'
    context_object_name = "albums"
    
@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = User
    form_class = ChangeUserDataForm
    template_name = 'update_profile.html'
    success_url  = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Account Updated Successfully')
        return super().form_valid(form)
    

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Logged Out Successfully')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UserPassChangeView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'passchange.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Enter Correct Password Format')
        return super().form_invalid(form)
    
