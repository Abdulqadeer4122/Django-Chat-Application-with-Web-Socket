from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def profile_view(request, username=None):
    if username:
        profile = User.objects.get(username__iexact=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')
    profile = request.user.profile
    return render(request, 'user/profile.html', {"profile": profile})


@login_required
def edit_profile_view(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    if request.path == reverse('profile_onboarding'):
        onboarding = True
    else:
        onboarding = False
    return render(request, 'user/profile_edit.html', {"form": form, 'onboarding': onboarding})


@login_required
def profile_setting_view(request):
    return render(request, 'user/profile_setting.html')


@login_required
def delete_profile(request):
    userp = request.user
    if request.method == 'POST':
        logout(request)
        userp.delete()
        messages.success(request, "account deleted successfully")
        return redirect('home_page')
    return render(request, 'user/profile_delete.html')
