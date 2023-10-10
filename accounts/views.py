from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from accounts.forms import LoginForm
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

def dashboard(request):
    return render(request, 'account/dashboard.html')