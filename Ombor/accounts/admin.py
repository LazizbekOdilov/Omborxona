from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class OmborAdmin(UserAdmin):
    model = Omborxona
    fieldsets = UserAdmin.fieldsets + (
        ('Ombor ustunlari', {
            'fields': ('ism', 'nom', "tel", "manzil")
        }),
    )
admin.site.register(Omborxona, OmborAdmin)