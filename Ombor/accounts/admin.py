from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class OmborAdmin(UserAdmin):
    model = Ombor
    fieldsets = UserAdmin.fieldsets + (
        ('Ombor ustunlari', {
            'fields': ('ism', 'nom', "tel", "manzil")
        }),
    )
admin.site.register(Ombor, OmborAdmin)