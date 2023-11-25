from django.shortcuts import render, redirect
from django.views import View
from .models import *
from accounts.models import *
from asosiy.models import *





class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                "statislar": Statistika.objects.filter(ombor=request.user),
                "mahsulotlar": Mahsulot.objects.filter(ombor=request.user),
                "mijozlar": Mijoz.objects.filter(ombor=request.user)
            }
            return render(request, "stats.html", data)
        return redirect("login")

    def post(self, request):
        Statistika.objects.create(
            mahsulot = request.user,
            mijoz = request.user,
            miqdor = request.POST.get("miqdor"),
            sana = request.POST.get("sana"),
            summa = request.POST.get("summa"),
            tolangan_summa = request.POST.get("tolangan_summa"),
            nasiya = request.POST.get("nasiya"),
            ombor = request.user
        )
        redirect("/asosiy/stats/")