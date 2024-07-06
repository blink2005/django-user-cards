from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

INVALID_USERNAME_OR_PASSWORD = 'Неверный юзернейм или пароль'

def login_user(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'authenticate_user/index.html')
        else:
            return HttpResponseRedirect('/')
        
    if request.method == 'POST':
        check_form = auth_user(request)
        if check_form is not None:
            login(request, check_form)
            return HttpResponseRedirect('/')
        else:
           return render(request, 'authenticate_user/index.html', context={'error': INVALID_USERNAME_OR_PASSWORD}) 
        
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def auth_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return authenticate(username=username, password=password)