from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import MyUser
from django.contrib.auth import authenticate
from django.core.mail import send_mail
class UserRegistrationForm(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput)
    password2=forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model=MyUser
        fields=('email','Uname','phone','age','country','company_name','password1','password2')
       
        widgets={
           'email':forms.TextInput(attrs={'class':'form-control'}),
           'Uname':forms.TextInput(attrs={'class':'form-control'}),
           'company_name':forms.TextInput(attrs={'class':'form-control'}),
           'phone':forms.TextInput(attrs={'class':'form-control'}),
           'age':forms.TextInput(attrs={'class':'form-control'}),
           'country':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class UserLoginForm(forms.ModelForm):
    password=forms.CharField(label="password",widget=forms.PasswordInput)

    class Meta:
        model=MyUser
        fields=('email', 'password')
    
    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']

            if not authenticate(email=email,password=password):
                raise forms.ValidationError("invalid credential") 

