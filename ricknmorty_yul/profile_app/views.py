from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView

from profile_app.forms import RegisterForm, LoginForm, ProfileForm

# Create your views here.
from profile_app.models import Profile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.warning(request, f"{form.cleaned_data['username']} is already in use")
                return redirect(reverse('profile_app:register'))
            user = User.objects.create_user(**form.cleaned_data)
            messages.info(request, f'{user.username} successfully created!')
            return redirect(reverse('profile_app:profile'))
    else:
        form = RegisterForm()

    return render(request, 'profile_app/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                messages.info(request, 'Successfully logged in!')
                return redirect(reverse('profile_app:profile'))
            else:
                messages.error(request, 'Bad authentication...')
                return redirect(reverse('profile_app:login'))
    else:
        form = LoginForm()

    return render(request, 'profile_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect(reverse('profile_app:login'))


class ProfileView(CreateView):
    form_class = ProfileForm
    template_name = 'profile_app/profile.html'
    success_url = 'profile_app:avatar_profile'


def MainProfileView():
    pass
# about page with cards in bootstrap


# class CreateProfile(CreateView):
#     form_class = ProfileForm
#     template_name = 'profile_app/profile.html'
#
#     def get_object(self, queryset=None):
#         return Profile.objects.get(pk=int(self.kwargs['pk']))
