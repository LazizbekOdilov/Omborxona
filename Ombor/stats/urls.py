from django.urls import path
from .views import *

urlpatterns = [
    path('statislar/', StatistikaView.as_view(), name="login"),
]
