from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import LoginForm, RegisterForm
from django.views.generic import (
    CreateView,
)


class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm  # 使用的表單類別
    template_name = 'create.html'
    success_url = '/account/login'  # 儲存成功後要導向的網址


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
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect('login')  # 重新導向到登入畫面
# Create your views here.

class Userlist(View):
    @method_decorator(login_required)
    def get(self, request):
        users = User.objects.all()
        user = request.user
        return render(request, 'Userlist.html', locals())
