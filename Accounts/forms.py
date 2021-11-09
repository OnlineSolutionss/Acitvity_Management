from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from Accounts.models import User_Profile

from blog import models


class User_Registeration(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter user name..'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password..'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password..'}))
    email  = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email id..'}))

    class Meata:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

        labels = {
            'password1': 'Enter Password',
            'password2: ': 'Confirm Password',
            'email':'E-Mail',
        
        }

class AddCustom_FieldsIn_UserForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput ,label='Confirm Password')
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']

        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'E-Mail',
            'password_confirmation':'Confirm Password'
        }

class Login_form_hai(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Username', 'autofocus':True}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password', 'autocomplete':'current-password' }))

class Change_Passwordsf(PasswordChangeForm):
    old_password = forms.CharField( strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old Password', 'autocomplete':'current-password' }))
    new_password1 = forms.CharField( strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password', 'autocomplete':'current-password' }))
    new_password2 = forms.CharField( strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password', 'autocomplete':'current-password' }))

    class Meta:

        labels = {
            'new_password1': 'New Password',
            'new_password2': 'Confirm Password',
        }

class Edit_Profile(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('image', 'about', 'city', 'state', 'country')


        # widgets = {
        #     'bio':forms.Textarea(attrs={'class': 'form-control'})
        # }

        # labels = {
        #     'bio': 'About: ',
        #     'image': 'Profile pic: ',
        #     'phone': 'Phone no: ',
        #     'address': 'Your Address',
        # }


class EditProfile_form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('image', 'about', 'city', 'state', 'country')

        

class MyPasswordResetForm(PasswordResetForm):
    email  = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Register email id..'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField( strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password', 'autocomplete':'current-password' }))
    new_password2 = forms.CharField( strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password', 'autocomplete':'current-password' }))

    class Meta:

        labels = {
            'new_password1': 'New Password',
            'new_password2': 'Confirm Password',
        }



