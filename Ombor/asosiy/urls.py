from django.urls import path
from .views import *

urlpatterns = [
    path("bolimlar/", Bolimlar.as_view()),
    path("mahsulotlar/", Mahsulotlar.as_view()),
    path("clentlar/", Mijozlar.as_view()),
]
