from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from accounts.forms import UserRegistrationForm
from accounts.models import Profile


# Create your views here.


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#         if user is not None:
#
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse('Вы залогинены')
#             else:
#                 return HttpResponse('Пользователь неактивен')
#         else:
#             return HttpResponse('Пользователь не найден')
#     form = LoginForm()
#     return render(request, 'registration/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = Profile
        if user_form.is_valid():



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {"user_form": user_form})

