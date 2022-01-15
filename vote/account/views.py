from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm , RegisterForm
from django.views.generic import (
    CreateView,
)


class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm  # 使用的表單類別
    template_name = 'create.html'
    success_url = '/account'  # 儲存成功後要導向的網址


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', locals())

    def post(self, request):
        form = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/votesystem')  # 重新導向到首頁
        return render(request, 'login.html', locals())


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('account/login')  # 重新導向到登入畫面
# Create your views here.
