from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View

from todo_auth.forms import CustomUserCreationForm, CustomAuthenticationForm


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        messages.error(request, f"{form.errors}")
        return redirect("register")


class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('read_todo')
        messages.error(request, message="login or password is not correct")
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('read_todo')
