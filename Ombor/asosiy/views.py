from django.shortcuts import render, redirect
from django.views import View
from .models import *
from datetime import date


class BolimlarView(View):
    def get(self, request):
        return render(request, "bulimlar.html")

    def post(self, request):
        pass


class MahsulotlarView(View):
    def get(self, request):
        content = {
            "mahsulotlar": Mahsulot.objects.filter(ombor=request.user),
            "nom": request.user.nom.capitalize()
        }
        return render(request, "products.html", content)

    def post(self, request):
        Mahsulot.objects.create(
            nom=request.POST.get("nom"),
            brend=request.POST.get("brend"),
            olchov=request.POST.get("olchov"),
            narx=request.POST.get("narx"),
            miqdor=request.POST.get("miqdor"),
            kelgan_sana=date.today(),
            ombor=request.user
        )
        return redirect("/asosiy/mahsulotlar/")


class MijozlarView(View):  # Vazifa 1
    def get(self, request):
        content = {
            "mijozlar": Mijoz.objects.filter(ombor=request.user),
            "nom": request.user.nom.capitalize()
        }
        return render(request, "clients.html", content)

    def post(self, request):
        Mijoz.objects.create(
            ism=request.POST.get("ism"),
            nom=request.POST.get("nom"),
            manzil=request.POST.get("manzil"),
            tel=request.POST.get("tel"),
            ombor=request.user
        )
        return redirect("/asosiy/clientlar/")


class MahsulotlarUpdateView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            product = Mahsulot.objects.get(id=son)
            if product.ombor == request.user:
                content = {
                    "mahsulot": Mahsulot.objects.get(id=son)
                }
                return render(request, "product_update.html", content)
            return redirect("/asosiy/mahsulotlar/")
        return redirect("/")

    def post(self, request, son):
        Mahsulot.objects.filter(id=son).update(
            nom=request.POST.get("nom"),
            brend=request.POST.get("brend"),
            narx=request.POST.get("narx"),
            miqdor=request.POST.get("miqdor"),
            kelgan_sana=date.today(),
            ombor=request.user
        )
        return redirect("/asosiy/mahsulotlar/")


class MijozlarUpdateView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            product = Mijoz.objects.get(id=son)
            if product.ombor == request.user:
                content = {
                    "mijoz": Mijoz.objects.get(id=son)
                }
                return render(request, "client_update.html", content)
            return redirect("/asosiy/clientlar/")
        return redirect("/")

    def post(self, request, son):
        Mijoz.objects.filter(id=son).update(
            ism=request.POST.get("ism"),
            nom=request.POST.get("nom"),
            manzil=request.POST.get("manzil"),
            tel=request.POST.get("tel"),
            ombor=request.user
        )
        return redirect("/asosiy/clientlar/")