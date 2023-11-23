from django.contrib import admin
from django.urls import path, include
from accounts.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name="login"),
    path('user/', include("accounts.urls")),
    path('asosiy/', include("asosiy.urls")),
    path('stats/', include("stats.urls")),
]
