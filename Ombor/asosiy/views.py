from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def builimlar(request):
    return render(request, "bulimlar.html")

def client_update(request):
    return render(request, "client_update.html")

def clients(request):
    return render(request, "clients.html")

def product(request):
    return render(request, "product_update.html")

def products(request):
    return render(request, "products.html")

def stats(request):
    return render(request, "stats.html")

