from django.shortcuts import render,redirect
from Authenticateapp.forms import UserForm,UserProfileForm,Updateform,UserProfileUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
            return redirect('login')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered,
    }
    return render(request,'register.html',context)

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request, "Your account is not active.")
        else:
            messages.error(request, "Invalid credentials. Please try again.")   

    return render(request,"login.html",{})


@login_required(login_url='login')
def home(request):
    return render(request,"index.html",{})
 
# logout view
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html',{})

@login_required(login_url='login')
def Update(request):
    if request.method=='POST':
        form = Updateform(request.POST,instance=request.user)
        form1=UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if form.is_valid() and form1.is_valid():
            user=form.save()
            user.save()

            profile=form1.save(commit=False)
            profile.user=user
            profile.save()
            return redirect('dashboard')
    else:
        form=Updateform(instance=request.user)  
        form1=UserProfileUpdateForm(instance=request.user.userprofile)
    return render(request,"update.html",{'form':form,'form1':form1})