from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.views import View


# Create your views here.

# class loginView(View):
#
def UserLogin(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'index.html', {})
    elif request.method == 'GET':
        return render(request, 'login.html', {})


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')



