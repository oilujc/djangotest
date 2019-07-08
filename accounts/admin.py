from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (User, )

# Register your models here.
class CustomUserAdmin(UserAdmin):
	fieldsets = UserAdmin.fieldsets + (
            ('Extra Fields', {
            'fields': (
                'image',
                'bio'
            	),
        }),
    )

admin.site.register(User, CustomUserAdmin)