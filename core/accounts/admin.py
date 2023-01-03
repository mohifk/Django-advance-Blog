from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        ('Authrntication', {'fields': ('email', 'password'),}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser'),}),
        ('group permissions', {'fields': ('groups', 'user_permissions'),}),
        ('important date', {'fields': ('last_login',),}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','is_superuser')}
        ),
    )

admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)

