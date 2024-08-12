from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
        self.fields['first_name'] = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
        self.fields['last_name'] = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
        self.fields['email'] = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    
    
class MyPasswordChangeForm(PasswordChangeForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].help_text = None

class ChangeUserDataForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        if 'password' in self.fields:
            del self.fields['password']