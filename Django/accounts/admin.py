from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']
    search_fields = ('username', 'email')
    ordering = ('email',)
    # extend the default UserAdmin fieldsets with extra fields
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('bio',)}),
    )


# register at module level
admin.site.register(CustomUser, CustomUserAdmin)
