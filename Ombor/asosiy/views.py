from django.shortcuts import render, redirect
from django.views import View
from .models import *

class Bolimlar(View):
    def get(selfs, request):
        if request.user.is_authenticated:
            return render(request, "bulimlar.html")
        redirect("login")

class Mahsulotlar(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                "mahsulotlar": Mahsulot.objects.filter(ombor=request.user)
            }
            return render(request, "products.html", content)
        redirect("login")

class Mijozlar(View):
    def get(self, request):
        return render(request, "clients.html")