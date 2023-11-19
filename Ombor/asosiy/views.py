from django.shortcuts import render
from django.views import View

class Bolimlar(View):
    def get(selfs, request):
        return render(request, "bulimlar.html")

class Mahsulotlar(View):
    def get(self, request):
        return render(request, "products.html")

class Mijozlar(View):
    def get(self, request):
        return render(request, "clients.html")