from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from userprofile.forms import RegistrationForm, ProfileForm
from django.contrib import messages

import os
from PIL import Image


# Create your views here.
# @login_required
def index(request):
    return render(request, 'index.html')


def register(request):
    # registered = False
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile_settings(request):
    return render(request, 'userprofile/profile.html')


@login_required
def edit_profile(request):
    user = request.user
    form = ProfileForm(instance=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_settings')

    context_dict = {'form': form}

    return render(request, 'userprofile/update_profile.html', context_dict)


def bug_report(request):
    return render(request, 'bugreport.html')


def download_profile_image(request):
    im = Image.open(settings.MEDIA_ROOT + "/" + str(request.user.profile.profile_image))
    im = im.save(os.environ['HOME'] + "/Downloads/profile_pic_download.jpg")

    return render(request, 'userprofile/profile.html')


def test(request):
    return render(request, 'test.html')

    #     form = RegForm(request.POST)

    #     profile_form = ProfileForm(request.POST, request.FILES)
    #     if form.is_valid() and profile_form.is_valid():
    #         user = form.save()
    #         user.set_password(user.password)
    #         user.save()
    #         profile = profile_form.save(commit=False)
    #         profile.user = user
    #         if 'photo' in request.FILES:
    #             print('Got it....')
    #             profile.photo = request.FILES['photo']
    #             print(request.FILES['photo'])
    #         profile.save()
    #         registered = True
    #         return redirect('index')
    # else:
    #     form = RegForm()
    #     profile_form = ProfileForm()
    #
    # return render(request, "userprofile/signup.html",
    #               {"form": form, "profile_form": profile_form, 'registered': registered})

# @login_required
# def logout(request):
#     auth.logout(request)
#     return render(request,'userprofile/index.html')


# #login to system
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('index')
#             else:
#                 messages.error(request, 'Your account was inactive !!!')
#         else:
#             print("They used username: {} and password: {}".format(username,password))
#             messages.error(request, 'Invalid login details given !!!')
#     else:
#         return render(request, 'userprofile/login.html', {})
