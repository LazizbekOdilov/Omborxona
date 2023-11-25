from django.urls import path
from .views import *

urlpatterns = [
    path("bolimlar/", BolimlarView.as_view(), name="sections"),
    path("mahsulotlar/", MahsulotlarView.as_view()),
    path("mijozlar/", MijozlarView.as_view()),
    path("mahsulotlar_update/<int:son>/", MahsulotlarUpdateView.as_view()),
    path("mijozlar_update/<int:son>/", MijozlarUpdateView.as_view())

]