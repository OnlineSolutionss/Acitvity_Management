from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,load_backend, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from .forms import EditProfile_form, User_Registeration,Login_form_hai,Change_Passwordsf,Edit_Profile
from django.contrib.auth.models import User
from .models import User_Profile
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

    # Sign-up
def Signup(request):
    if not  request.user.is_authenticated:
        if request.method == 'POST':
            fm = User_Registeration(request.POST)
            if fm.is_valid():
                print('Data is Valid')
                fm.save()
                messages.success(request,'Your Account is Successfuly Created')
                messages.info(request,'Now You Can Login to Your Account')
                return redirect('/login/')
        else:
            fm = User_Registeration()    
        return render(request, 'myapp/signup.html',{'form':fm})

    else:
        return redirect('dashboard')

# Login function View
def User_login(request):
    if not  request.user.is_authenticated:
        if request.method == 'POST':
            fm = Login_form_hai(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data.get('username')
                upassword = fm.cleaned_data.get('password')
                # Authenticating the user data is matching or not
                user = authenticate(username=uname,password=upassword)
                 # Calling/Making Login Request by using(login,request,uservar)
                if user is not None:
                    login(request,user)
                    messages.success(request,'You Have Successfuly Login To Your Account')
                    return redirect('dashboard')
        else:
            fm = Login_form_hai()
        return render(request,'myapp/login.html',{'form':fm})
    else:
        return render(request,'myapp/profile.html',{'name':request.user})

# Logout Functions
def User_Logout(request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')
        else:
            return redirect('/login/')
    
# Login to User Profile Dashboard
def User_Dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard/dashboard.html',{'name':request.user})
        
    else:
        return redirect('login')

# Change Password By Old Password
def Change_Password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = Change_Passwordsf(user=request.user, data=request.POST)
            print(fm)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Your Password Changed Successfuly')
                return redirect('dashboard')
            else:
                print('Not Valid')
        else:
            fm = Change_Passwordsf(user=request.user)
        return render(request,'myapp/changepasswd.html',{'form':fm})
    else:
        return redirect('login')


def EditProfiles(request):
    user_id = request.user.id
    print(user_id)
    if user_id:
        profiles = User_Profile.objects.get(pk=user_id)
        if request.method == 'POST':
            form = EditProfile_form(request.POST, request.FILES, instance=profiles)
            if form.is_valid():
                form.save()
                return redirect('/')
            pass
        else:
            profiles = User_Profile.objects.get(pk=user_id)
            form = EditProfile_form(instance=profiles)
            return render(request, 'profile/editprofile.html',{'form':form})

