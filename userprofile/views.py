from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from userprofile.forms import RegForm, ProfileForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'userprofile/index.html')

def register(request):
    registered = False
    if request.method == "POST":
        form = RegForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'photo' in request.FILES:
                print('Got it....')
                profile.photo = request.FILES['profile/']
            profile.save()
            registered = True
            return redirect('index')
    else:
        form = RegForm()
        profile_form = ProfileForm()
    return render(request, "userprofile/signup.html", {"form":form, "profile_form":profile_form, 'registered':registered})
#login to system
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Your account was inactive !!!')
        else:
            print("They used username: {} and password: {}".format(student_id,password))
            messages.error(request, 'Invalid login details given !!!')
    else:
        return render(request, 'userprofile/login.html', {})

@login_required
def logout(request):
    auth.logout(request)
    return render(request,'userprofile/index.html')
