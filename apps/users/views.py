from django.shortcuts import render
from django.views.generic.base import View #基于类的视图
from django.contrib.auth import authenticate, login #自动登录和验证函数
from django.contrib.auth.hashers import make_password #

from .forms import RegisterForm, LoginForm
from .models import UserProfile

# Create your views here.

# class loginView(View):
#
def UserLogin(request):
    '''基于函数的登录'''
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {})
            return render(request, 'index.html', {'msg': '用户名/密码错了'})
        else:
            return render(request, 'login.html', {'login_form': login_form})
    elif request.method == 'GET':
        return render(request, 'login.html', )


class RegisterView(View):
    '''基于类的注册'''
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = UserProfile()
            user.username = user_name
            user.email = user_name
            user.password = make_password(pass_word)
            user.save()






