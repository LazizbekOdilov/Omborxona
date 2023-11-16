from django.contrib import admin
from django.urls import path

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('bulimlar/', builimlar),
    path('client/', client_update),
    path('clients/', clients),
    path('product/', product),
    path('products/', products),
    path('stats/', stats),
]
