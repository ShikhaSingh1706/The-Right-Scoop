from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import UserForm, UserProfileForm
from .models import Profile


# Create your views here.

class DashboardHomeView(LoginRequiredMixin,View):
    login_url = '/login/'

    def get(self,request):
        return render(request, 'user_dashboard/dashboard.html')


class ProfileView(LoginRequiredMixin,View):
    login_url = '/login/'

    def get(self, request):
        user = request.user
        profile = getattr(user, 'userprofile', None)  # safely get UserProfile if exists
        return render(request, 'user_dashboard/profile_view.html', {'user': user, 'profile': profile})


class ProfileEditView(LoginRequiredMixin,View):
    login_url = '/login/'

    def get(self, request):
        user = request.user
        profile = getattr(user, 'userprofile', None)
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)
        return render(request, 'user_dashboard/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user = request.user
        profile = getattr(user, 'userprofile', None)
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('dashboard:profile_view')
        
        return render(request, 'dashboard/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})


   