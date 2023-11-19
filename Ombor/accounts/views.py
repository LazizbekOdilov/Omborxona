from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .models import *
class Login(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        user = authenticate(
            login = request.POST.get("l"),
            password= request.POST.get("p")
        )
        return render(request, "bulimlar.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")



