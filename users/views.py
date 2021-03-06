from django.shortcuts import redirect, render
from .forms import RegisterFormUser,UserUpdateForm,ProfilePicUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterFormUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created successfully!. Please Login.')
            return redirect('login')
    else:
        form = RegisterFormUser()
    return render(request,'users/register.html',{'form':form})

@login_required()
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfilePicUpdate(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account has been updates successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilePicUpdate(instance=request.user.profile)

    return render(request,'users/profile.html',{'u_form':u_form,'p_form':p_form})



